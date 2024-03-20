from typing import Optional
import typer
from pathlib import Path
from spacy_llm.util import assemble
from wasabi import msg
import pandas as pd

Arg = typer.Argument
Opt = typer.Option


def process_text_file(
    file_path: Path, 
    nlp, 
    output_dir: Path
):
    with open(file_path, 'r') as file:
        text = file.read()
        doc = nlp(text)

        entities = [(ent.text, ent.label_) for ent in doc.ents]
        df = pd.DataFrame(entities, columns=['Text', 'Label'])
        output_file = output_dir / f"{file_path.stem}_entities.csv"
        df.to_csv(output_file, index=False)
        msg.good(f"Processed {file_path} and saved entities to {output_file}")


def run_pipeline(
    # fmt: off
    input_dir: Path = Arg(..., help="Directory containing text files with GSoC ideas."),
    config_path: Path = Arg(..., help="Path to the configuration file to use."),
    examples_path: Optional[Path] = Arg(None, help="Path to the examples file to use (few-shot only)."),
    output_dir: Path = Opt(Path("./output"), "--output-dir", "-o", help="Directory to save the CSV files."),
    verbose: bool = Opt(False, "--verbose", "-v", help="Show extra information."),
    # fmt: on
):
    msg.text(f"Loading config from {config_path}", show=verbose)
    nlp = assemble(
        config_path,
        overrides={}
        if examples_path is None
        else {"paths.examples": str(examples_path)},
    )

    output_dir.mkdir(exist_ok=True)

    for file_path in input_dir.glob("*.txt"):
        process_text_file(file_path, nlp, output_dir)


if __name__ == "__main__":
    typer.run(run_pipeline)
