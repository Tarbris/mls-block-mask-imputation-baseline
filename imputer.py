"""Weak column-mean starter; edit only this file."""


class Imputer:
    def fit(self, rows):
        width = len(rows[0])
        self.means = []
        for col in range(width):
            values = [row[col] for row in rows if row[col] is not None]
            self.means.append(sum(values) / len(values) if values else 0.0)
        return self

    def transform(self, rows):
        return [[self.means[j] if value is None else value
                 for j, value in enumerate(row)] for row in rows]
