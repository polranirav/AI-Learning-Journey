Extract → Clean/Engineer → Train → Generate

Phase 1 CLI:
- preset_extract: reads `config/extract.yaml`, scans `data/raw/{xmp,lrtemplate}`
- Writes CSV/JSONL to `data/processed/`

