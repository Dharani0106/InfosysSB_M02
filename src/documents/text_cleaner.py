import re

class TextCleaner:

    @staticmethod
    def clean_text(text):
        """
        Clean extracted PDF text.
        """
        if not text:
            return ""

        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            # Replace tabs with spaces
            cleaned_line = re.sub(r"\t+", " ", line)
            # Remove non-printable characters
            cleaned_line = "".join(
                ch for ch in cleaned_line
                if ch.isprintable()
            )
            # Remove unnecessary spaces
            cleaned_line = cleaned_line.strip()
            # Keep only non-empty lines
            if cleaned_line:
                cleaned_lines.append(cleaned_line)

        return "\n".join(cleaned_lines)