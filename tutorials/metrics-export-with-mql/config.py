# Replace the values as needed
PROJECT_ID = "ust-edgeops-dagility-dev"
PUBSUB_TOPIC = "mql_metric_export"
BIGQUERY_DATASET = "metric_export"
BIGQUERY_CLUSTER_TABLE = "gkecluster_metrics"
BIGQUERY_DATAFLOW_TABLE = "dataflow_metrics"
BIGQUERY_KUBERNETES_TABLE = "kubernetes_metrics"
BIGQUERY_BIGTABLE_TABLE = "bigtable_metrics"

# Add/Update the queries for your metrics
MQL_QUERYS = {
#"instance/cpu/utilization":
#"""
#fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
#| bottom 3, max(val()) | within 5m
#""",
# "instance/gkecluster/bytecount":
# """
# fetch k8s_cluster
# | metric 'logging.googleapis.com/byte_count'
# | align rate(1h)
# | every 1h
# """,
# "instance/gkecluster/logentrycount":
# """
# fetch k8s_cluster
# | metric 'logging.googleapis.com/log_entry_count'
# | align rate(1h)
# | every 1h
# """,
# "instance/dataflow/logentrycount":
# """
# fetch dataflow_job
# | metric 'logging.googleapis.com/log_entry_count'
# | align rate(96h)
# | every 96h
# """,
# "instance/dataflow/bytecount":
# """
# fetch dataflow_job
# | metric 'logging.googleapis.com/byte_count'
# | align rate(96h)
# | every 96h
# """,
# "instance/bigtable/requestcount":
# """
# fetch bigtable_table
# | metric 'bigtable.googleapis.com/server/request_count'
# | align rate(5h)
# | every 5h
# """,
# "instance/bigtable/bytescount":
# """
# fetch bigtable_table
# | metric 'bigtable.googleapis.com/table/bytes_used'
# | group_by 5m, [value_bytes_used_mean: mean(value.bytes_used)]
# | every 5m
# """,
# "instance/bigtable/storageutilization":
# """
# fetch bigtable_cluster
# | metric 'bigtable.googleapis.com/cluster/storage_utilization'
# | group_by 1h, [value_storage_utilization_mean: mean(value.storage_utilization)]
# | every 1h
# """,
# "instance/bigtable/pernodestoragecapacity":
# """
# fetch bigtable_cluster
# | metric 'bigtable.googleapis.com/disk/per_node_storage_capacity'
# | group_by 1h,
#     [value_per_node_storage_capacity_mean:
#        mean(value.per_node_storage_capacity)]
# | every 1h
# """,
# "instance/bigtable/bytesused":
# """
# fetch bigtable_cluster
# | metric 'bigtable.googleapis.com/disk/bytes_used'
# | group_by 1h, [value_bytes_used_mean: mean(value.bytes_used)]
# | every 1h
# """,
# "instance/bigtable/storagecapacity":
# """
# fetch bigtable_cluster
# | metric 'bigtable.googleapis.com/disk/storage_capacity'
# | group_by 1h, [value_storage_capacity_mean: mean(value.storage_capacity)]
# | every 1h
# """,
# "instance/kubernetes/nodesbytecount":
# """
# fetch k8s_node
# | metric 'logging.googleapis.com/byte_count'
# | align rate(5h)
# | every 5h
# """,
# "instance/kubernetes/nodelogentrycount":
# """
# fetch k8s_node
# | metric 'logging.googleapis.com/log_entry_count'
# | align rate(5h)
# | every 5h
# """

#DFDS Metrics

"instance/dataflow/total_shuffle_data_processed":
"""
fetch dataflow_job
| metric 'dataflow.googleapis.com/job/total_shuffle_data_processed'
| group_by 30d,
    [value_total_shuffle_data_processed_mean:
       mean(value.total_shuffle_data_processed)]
| every 30d
| group_by [resource.job_name],
    [value_total_shuffle_data_processed_mean_aggregate:
       aggregate(value_total_shuffle_data_processed_mean)]""",

"instance/dataflow/total_streaming_data_processed":
"""	   
fetch dataflow_job
| metric 'dataflow.googleapis.com/job/total_streaming_data_processed'
| group_by 30d,
    [value_total_streaming_data_processed_mean:
       mean(value.total_streaming_data_processed)]
| every 30d
| group_by [resource.job_name],
    [value_total_streaming_data_processed_mean_aggregate:
       aggregate(value_total_streaming_data_processed_mean)]""",
	   
	   
	   
"instance/bigtable/received_bytes_count":	   
"""fetch bigtable_table
| metric 'bigtable.googleapis.com/server/received_bytes_count'
| align rate(30d)
| every 30d
| group_by [resource.table],
    [value_received_bytes_count_aggregate:
       aggregate(value.received_bytes_count)]""",
	   
"instance/bigtable/sent_bytes_count":	   
"""fetch bigtable_table
| metric 'bigtable.googleapis.com/server/sent_bytes_count'
| align rate(30d)
| every 30d
| group_by [resource.table],
    [value_sent_bytes_count_aggregate: aggregate(value.sent_bytes_count)]""",
	
"instance/bigtable/bytes_used":	   
"""	
fetch bigtable_table
| metric 'bigtable.googleapis.com/table/bytes_used'
| group_by 1h, [value_bytes_used_max: max(value.bytes_used)]
| every 1h
| group_by [resource.table],
    [value_bytes_used_max_max: max(value_bytes_used_max)]""",
	
"instance/bigtable/request_count":	   
"""	
fetch bigtable_table
| metric 'bigtable.googleapis.com/server/request_count'
| align rate(72h)
| every 72h
| group_by [resource.table],
    [value_request_count_aggregate: aggregate(value.request_count)]""",
	
	
"instance/gkecluster/total_bytes":
"""
fetch gcs_bucket
| metric 'storage.googleapis.com/storage/total_bytes'
| group_by 30d, [value_total_bytes_max: max(value.total_bytes)]
| every 30d
| group_by [resource.bucket_name],
    [value_total_bytes_max_max: max(value_total_bytes_max)]""",

"instance/gkecluster/object_count":
"""	
fetch gcs_bucket
| metric 'storage.googleapis.com/storage/object_count'
| group_by 30d, [value_object_count_max: max(value.object_count)]
| every 30d
| group_by [resource.bucket_name],
    [value_object_count_max_max: max(value_object_count_max)]""",
	

"instance/gkecluster/received_bytes_count":
"""
fetch gcs_bucket
| metric 'storage.googleapis.com/network/received_bytes_count'
| align rate(72h)
| every 72h
| group_by [resource.bucket_name],
    [value_received_bytes_count_aggregate:
       aggregate(value.received_bytes_count)]""",
	   
"instance/gkecluster/sent_bytes_count":
"""
fetch gcs_bucket
| metric 'storage.googleapis.com/network/sent_bytes_count'
| align rate(72h)
| every 72h
| group_by [resource.bucket_name],
    [value_sent_bytes_count_aggregate: aggregate(value.sent_bytes_count)]""",

#ADDITIONAL METRICS

"instance/bigtable/node_count":	   
"""	
fetch bigtable_cluster
| metric 'bigtable.googleapis.com/cluster/node_count'
| group_by 1h, [value_node_count_max: max(value.node_count)]
| every 1h
| group_by [resource.cluster],
    [value_node_count_max_max: max(value_node_count_max)]""",
	
"instance/dataflow/total_vcpu_time":
"""	   
fetch dataflow_job
| metric 'dataflow.googleapis.com/job/total_vcpu_time'
| group_by 30d, [value_total_vcpu_time_mean: mean(value.total_vcpu_time)]
| every 30d
| group_by [resource.job_name],
    [value_total_vcpu_time_mean_mean: mean(value_total_vcpu_time_mean)]""",

"instance/dataflow/current_num_vcpus":
"""	   
fetch dataflow_job
| metric 'dataflow.googleapis.com/job/current_num_vcpus'
| group_by 30d, [value_current_num_vcpus_mean: mean(value.current_num_vcpus)]
| every 30d
| group_by [resource.job_name],
    [value_current_num_vcpus_mean_mean: mean(value_current_num_vcpus_mean)]""",
	
"instance/dataflow/memory_capacity":
"""	   
fetch dataflow_job
| metric 'dataflow.googleapis.com/job/memory_capacity'
| group_by 30d, [value_memory_capacity_mean: mean(value.memory_capacity)]
| every 30d
| group_by [resource.job_name],
    [value_memory_capacity_mean_mean: mean(value_memory_capacity_mean)]"""





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
