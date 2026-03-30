import json

class DataIndexer:
    def __init__(self):
        self.index = {}

    def load_data(self, filepath):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"error loading file: {e}")
            return {}

    def normalize(self, value):
        if isinstance(value, str):
            return value.strip().lower()
        return str(value)

    def build_index(self, data):
        for key, value in data.items():
            norm_val = self.normalize(value)
            self.index[key] = {
                "value": norm_val,
                "length": len(norm_val)
            }

    def search(self, query):
        results = {}
        query = query.lower()
        for key, value in self.index.items():
            if query in value["value"]:
                results[key] = value
        return results

    def summary(self):
        return {
            "total_entries": len(self.index),
            "keys": list(self.index.keys())
        }


if __name__ == "__main__":
    indexer = DataIndexer()

    sample_data = {
        "Name": "Example Data",
        "Type": "Test",
        "Category": "Sample Entry",
        "Status": "Incomplete"
    }

    indexer.build_index(sample_data)

    print("Index Summary:")
    print(indexer.summary())

    print("\nSearch Results:")
    results = indexer.search("sample")
    print(results)
