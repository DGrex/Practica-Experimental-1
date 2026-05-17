import json

class ExportMixin:
    def export_json(self, data: list[dict]) -> str:
        return json.dumps(data, indent=4)

    def export_csv(self, data: list[dict]) -> str:
        if not data:
            return ""
        headers = data[0].keys()
        lines = [",".join(headers)]
        for d in data:
            lines.append(",".join(str(d[h]) for h in headers))
        return "\n".join(lines)

class Report(ExportMixin):
    def __init__(self, data: list[dict]):
        self.data = data

    def show_exports(self):
        print("JSON:")
        print(self.export_json(self.data))
        print("\nCSV:")
        print(self.export_csv(self.data))
        


sales = [
    {"producto": "Laptop", "precio": 1200},
    {"producto": "Mouse", "precio": 25}
]

report = Report(sales)
report.show_exports()
