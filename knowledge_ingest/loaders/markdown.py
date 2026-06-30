"""
knowledge_ingest.loaders.markdown

Markdown Loader

Responsibility:
    Read a markdown file from disk.

Ownership:
    Markdown File
            ↓
        Raw Text

Nothing else.

This loader DOES NOT:
- chunk
- embed
- clean text
- understand markdown
"""

from pathlib import Path

from knowledge_ingest.exceptions import LoaderError


class MarkdownLoader:
    """
    Loads markdown documents into memory.
    """

    SUPPORTED_EXTENSIONS = {".md", ".markdown"}

    def load(self, path: str) -> tuple[str, str]:
        """
        Returns
        -------
        tuple[text, source]

        text:
            Entire markdown file as a string.

        source:
            Filename only.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise LoaderError(f"File not found: {path}")

        if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise LoaderError(
                f"Unsupported file type: {file_path.suffix}"
            )

        try:
            text = file_path.read_text(
                encoding="utf-8"
            )

            return (
                text,
                file_path.name,
            )

        except Exception as e:
            raise LoaderError(
                f"Unable to read '{path}': {e}"
            ) from e