# seosiri-semantic-entity-mcp

> 📖 **Official Architecture & Documentation:** [SEOSiri Semantic Entity Guide](https://www.seosiri.com/2026/08/semantic-entity-mcp.html) | [Central MCP Directory](https://www.seosiri.com/2026/07/seosiri-mcp-servers.html)

An open-source, local-first Model Context Protocol (MCP) server for **Named Entity Extraction, Wikidata Disambiguation, sameAs Schema Linking, and Knowledge Graph Triple Construction**.

## 💖 Sponsorship, B2B Custom Solutions & Attribution

### 👨‍💻 Lead Architect & Attribution
Designed and engineered by **[Momenul Ahmad](https://github.com/MOBILEPHONE)**, Lead Architect and Founder of **[SEOSiri](https://seosiri.com)**.

### 🚀 Capabilities & Tools (10 Production Tools)
- **`extract_named_entities`**: Scrapes and parses text content to identify named entities.
- **`disambiguate_wikidata_entity`**: Resolves entity names to canonical Wikidata QIDs.
- **`generate_sameas_schema_links`**: Compiles structured `sameAs` array mappings for Schema.org JSON-LD.
- **`calculate_entity_salience_score`**: Scores relative entity importance within a document.
- **`construct_knowledge_graph_triples`**: Generates Subject-Predicate-Object ($S \rightarrow P \rightarrow O$) semantic triples.
- **`audit_entity_density_ratio`**: Evaluates entity frequency per 100 words.
- **`export_graph_parquet_buffer`**: Formats knowledge graph triples into columnar Parquet buffers.
- **`sanitize_entity_payload`**: Strips script injections and malformed tags.
- **`get_live_entity_throughput_metrics`**: Monitors system health and processing latency.
- **`get_entity_server_specifications`**: Returns protocol specs and capability matrices.

## Quickstart

```bash
pip install -e .
pytest tests/test_semantic_entity.py
```

### 🔌 Claude Desktop / Cursor Configuration
Add this block to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "seosiri-semantic-entity": {
      "command": "uv",
      "args": [
        "run",
        "--github",
        "SEOSiri-Official/semantic-entity-mcp",
        "src/main_server.py"
      ]
    }
  }
}
```

## License
Distributed under the MIT License. See [LICENSE](https://github.com/SEOSiri-Official/semantic-entity-mcp/blob/main/LICENSE) for more details.
