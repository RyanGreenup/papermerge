worker_concurrency = 1
broker_url = "filesystem://"
broker_transport_options = {
    'data_folder_in': '{{proj_root}}/run/broker/data_out',
    'data_folder_out': '{{proj_root}}/run/broker/data_out',
    'data_folder_processed': '{{proj_root}}/run/broker/data_processed',
}
worker_hijack_root_logger = True
task_default_exchange = 'papermerge'
task_ignore_result = False
result_expires = 86400
result_backend = 'rpc://'
include = 'pmworker.tasks'
accept_content = ['pickle', 'json']
s3 = False
s3_storage = "s3:/..."  # does not matter in dev
local_storage = "local:/{{media_root}}/"
