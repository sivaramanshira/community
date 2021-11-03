# Replace the values as needed
PROJECT_ID = "$PROJECT_ID"
PUBSUB_TOPIC = "$PUBSUB_TOPIC"
BIGQUERY_DATASET = "$BIGQUERY_DATASET"
BIGQUERY_TABLE = "$BIGQUERY_TABLE"

# Add/Update the queries for your metrics
MQL_QUERYS = {
#"instance/cpu/utilization":
#"""
#fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
#| bottom 3, max(val()) | within 5m
#""",
"instance/gkecluster/bytecount":
"""
fetch k8s_cluster
| metric 'logging.googleapis.com/byte_count'
| align rate(1h)
| every 1h
""",
"instance/gkecluster/logentrycount":
"""
fetch k8s_cluster
| metric 'logging.googleapis.com/log_entry_count'
| align rate(1h)
| every 1h
""",
"instance/dataflow/logentrycount":
"""
fetch dataflow_job
| metric 'logging.googleapis.com/log_entry_count'
| align rate(1h)
| every 1h
""",
"instance/dataflow/bytecount":
"""
fetch dataflow_job
| metric 'logging.googleapis.com/byte_count'
| align rate(1h)
| every 1h
""",
"instance/bigtable/requestcount":
"""
fetch bigtable_table
| metric 'bigtable.googleapis.com/server/request_count'
| align rate(1h)
| every 1h
""",
"instance/bigtable/bytescount":
"""
fetch bigtable_table
| metric 'bigtable.googleapis.com/table/bytes_used'
| group_by 1h, [value_bytes_used_mean: mean(value.bytes_used)]
| every 1h
""",
"instance/bigtable/storageutilization":
"""
fetch bigtable_cluster
| metric 'bigtable.googleapis.com/cluster/storage_utilization'
| group_by 1h, [value_storage_utilization_mean: mean(value.storage_utilization)]
| every 1h
""",
"instance/bigtable/pernodestoragecapacity":
"""
fetch bigtable_cluster
| metric 'bigtable.googleapis.com/disk/per_node_storage_capacity'
| group_by 1h,
    [value_per_node_storage_capacity_mean:
       mean(value.per_node_storage_capacity)]
| every 1h
""",
"instance/bigtable/bytesused":
"""
fetch bigtable_cluster
| metric 'bigtable.googleapis.com/disk/bytes_used'
| group_by 1h, [value_bytes_used_mean: mean(value.bytes_used)]
| every 1h
""",
"instance/bigtable/storagecapacity":
"""
fetch bigtable_cluster
| metric 'bigtable.googleapis.com/disk/storage_capacity'
| group_by 1h, [value_storage_capacity_mean: mean(value.storage_capacity)]
| every 1h
""",
"instance/kubernetes/nodesbytecount":
"""
fetch k8s_node
| metric 'logging.googleapis.com/byte_count'
| align rate(1h)
| every 1h
""",
"instance/kubernetes/nodelogentrycount":
"""
fetch k8s_node
| metric 'logging.googleapis.com/log_entry_count'
| align rate(1h)
| every 1h
"""

# "bigquery/slots/total_available":
# """
# fetch global
# | metric 'bigquery.googleapis.com/slots/total_available'
# | group_by 5m, [value_total_available_mean: mean(value.total_available)]
# | every 5m | within 1h
# """,

# "bigquery/slots/allocated_for_project":
# """
# fetch global
# | metric 'bigquery.googleapis.com/slots/allocated_for_project'
# | group_by 5m,
#     [value_allocated_for_project_mean: mean(value.allocated_for_project)]
# | every 5m | within 1h
# """
}

BASE_URL = "https://monitoring.googleapis.com/v3/projects"
QUERY_URL = f"{BASE_URL}/{PROJECT_ID}/timeSeries:query"


BQ_VALUE_MAP = {
    "INT64": "int64_value",
    "BOOL": "boolean_value",
    "DOUBLE": "double_value",
    "STRING": "string_value",
    "DISTRIBUTION": "distribution_value"
}

API_VALUE_MAP = {
    "INT64": "int64Value",
    "BOOL": "booleanValue",
    "DOUBLE": "doubleValue",
    "STRING": "stringValue",
    "DISTRIBUTION": "distributionValue"
}
