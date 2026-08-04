# tests/test_semantic_entity.py
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main_server import (
    extract_named_entities,
    disambiguate_wikidata_entity,
    generate_sameas_schema_links,
    calculate_entity_salience_score,
    construct_knowledge_graph_triples,
    audit_entity_density_ratio,
    export_graph_parquet_buffer,
    sanitize_entity_payload,
    get_live_entity_throughput_metrics,
    get_entity_server_specifications
)


def test_1_extract_entities():
    res = json.loads(extract_named_entities("Momenul Ahmad founded SEOSiri using Python."))
    assert res["status"] == "EXTRACTED"


def test_2_disambiguate_wikidata():
    res = json.loads(disambiguate_wikidata_entity("Python"))
    assert res["status"] == "DISAMBIGUATED"
    assert "wikidata_url" in res


def test_3_sameas_links():
    res = json.loads(generate_sameas_schema_links("Python", "Q28865"))
    assert res["status"] == "GENERATED"
    assert len(res["sameAs"]) == 2


def test_4_entity_salience():
    res = json.loads(calculate_entity_salience_score("SEOSiri", "SEOSiri is an open source platform. SEOSiri builds MCP servers."))
    assert res["status"] == "SCORED"


def test_5_knowledge_graph_triples():
    res = json.loads(construct_knowledge_graph_triples("seosiri-semantic-entity-mcp", "usesProtocol", "Model Context Protocol"))
    assert res["status"] == "TRIPLE_STORED"


def test_6_entity_density():
    res = json.loads(audit_entity_density_ratio(10, 200))
    assert res["status"] == "AUDITED"


def test_7_parquet_export():
    construct_knowledge_graph_triples("Subject", "Predicate", "Object")
    res = json.loads(export_graph_parquet_buffer(10))
    assert res["status"] == "PARQUET_BUFFER_GENERATED"


def test_8_sanitize_payload():
    res = json.loads(sanitize_entity_payload("text <script>alert('xss')</script>"))
    assert res["status"] == "SANITIZED"


def test_9_throughput_metrics():
    res = json.loads(get_live_entity_throughput_metrics())
    assert res["status"] == "HEALTHY"


def test_10_server_specs():
    res = json.loads(get_entity_server_specifications())
    assert res["total_tools"] == 10