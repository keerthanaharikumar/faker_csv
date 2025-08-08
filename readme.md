# Faker CSV Generator — README

> 🎲 Turn fake data needs into instant CSVs — fast, fun, and totally synthetic!

This tiny Python tool uses **Faker** to generate CSV files filled with realistic-looking (but fake) data. Want a quick dataset to test forms, demos, or tutorials? This script does exactly that: pick what fields you want, how many rows, and it writes a CSV for you.

# What it does (short & sweet)
- Generates a CSV with any combination of Faker providers (like `name`, `email`, `address`, etc.).
- Provides a few special built-in fields: `id`, `number`, `float`, `boolean`.
- Can list all available Faker methods so you don’t have to guess names.
- Saves the generated rows to a CSV file you choose.

# Requirements
Install dependencies from your `requirements.txt`:

```bash
pip install -r requirements.txt
```


# Quickstart
Generate a CSV with 10 rows that contains `id`, `name`, and `email`:

```bash
python faker_csv.py --row 10 --field id name email --output demo.csv
```

List all available Faker provider methods:

```bash
python faker_csv.py --list
```

# Command-line arguments
- `--row` (int) — Number of rows to create (required unless using `--list`).
- `--field` (one or more values) — Fields/providers to include in the CSV header (required unless using `--list`).
- `--output` (string) — Path to the output CSV file (required unless using `--list`).
- `--list` (flag) — Print all available Faker provider methods (read-only mode).

# Special fields
These are handled by the script itself (not Faker methods):
- `id` — sequential integer starting at 1
- `number` — random integer (via Faker)
- `float` — random float (via Faker)
- `boolean` — random boolean (via Faker)

# How to pick field names
- Use Faker provider names (common ones: `name`, `first_name`, `last_name`, `email`, `address`, `phone_number`, `company`, `job`, `date`, etc.).
- The script will call each provider, so the name must match a callable attribute on `faker.Faker()` (case-sensitive).
- If a field is not found on the Faker instance, the script prints an error and stops.

# Example usage & expected output
Command:

```bash
python faker_csv.py --row 3 --field id name email boolean --output sample.csv
```

`sample.csv` might look like:

```csv
id,name,email,boolean
1,John Doe,john.doe@example.com,True
2,Jane Smith,jane.smith@example.org,False
3,Alex Roe,alex.roe@example.net,True
```

# Notes & gotchas
- `--list` bypasses validation — it only prints available provider names.
- Make sure provider names are valid Faker methods. If you pass an invalid name, the script will show: `Error: Faker has no provider named '...'`.
- The `id` column is generated sequentially from `1` to `--row`.
- The script writes UTF-8 CSVs and uses `newline=''` for cross-platform compatibility.
- Output file will be overwritten without prompt if it already exists.

# Troubleshooting
- `ModuleNotFoundError: No module named 'faker'` → run `pip install -r requirements.txt`.
- If a field produces unexpected values, check the Faker docs or try a different provider name.

# Extending this tool
Want more features? Consider adding:
- JSON or SQL output options
- Column value constraints (e.g., min/max for numbers, ranges for dates)
- Locale support (e.g., `Faker(locale='de_DE')`)
- Custom providers or a config file to define complex records


Enjoy your fake data playground — and remember, it’s all pretend. 😉




