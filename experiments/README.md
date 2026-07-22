# Experiments

Each experiment belongs in a dated directory:

```text
experiments/YYYY-MM-DD-short-name/
```

Recommended contents:

```text
README.md          Research question and parameter choices
commands.txt       Exact commands
results.jsonl      Raw machine-readable output
summary.md         Finite observations and limitations
environment.txt    Python, package, operating-system, and hardware details
```

## Minimum standard

A record is complete only when another person can rerun it from a named commit. Preserve raw results, including negative or inconvenient outcomes.

Every summary must distinguish:

- implementation validation;
- finite numerical observation;
- statistical description;
- conjectural interpretation;
- rigorous proof.
