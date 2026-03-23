import logging
import yaml
from beacon.request.classes import ErrorClass

try:
    with open("beacon/conf/api_version.yml") as api_version_file:
        api_version_yaml = yaml.safe_load(api_version_file)
except Exception as e:# pragma: no cover
    ErrorClass.error_code=500
    ErrorClass.error_message='There are issues with the api_version.yml file. Check if it can be opened or if has any content'
    raise

level=logging.NOTSET
log_file=None
beacon_id="org.garvan.rddp-beacon"
beacon_name="Garvan RDDP cohort-level beacon"
api_version = 'v2.0.0' # Version of the Beacon implementation
uri = 'http://localhost:5050'
uri_subpath = '/api'
complete_url = uri + uri_subpath
environment = 'test'
description = r"This Beacon is an experimental cohort-level beacon."
version = api_version_yaml['api_version']
welcome_url = 'https://beacon.ega-archive.org/'
alternative_url = 'https://beacon.ega-archive.org/api'
create_datetime = '2025-07-01T12:00:00.000000'
update_datetime = ''
default_beacon_granularity = "boolean" # boolean, count or record
security_levels = ['PUBLIC']
documentation_url = 'https://b2ri-documentation-demo.ega-archive.org/'
cors_urls = ["http://localhost:3003", "http://localhost:3000"]

# Service Info
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Organization info
org_id="Garvan"
org_name="Garvan Institute for Medical Research"
org_description="Garvan Institute of Medical Research is one of Australia’s premier medical research institutes"
org_adress = '384 Victoria Street, Darlinghurst NSW 2010, Australia'
org_welcome_url="https://garvan.org.au"
org_contact_url="mailto:dsp@garvan.org.au"
org_logo_url="https://images.contentstack.io/v3/assets/blt324fd0a04af716e6/blt3f0048229394c515/6405de96205f2b7a60b745d6/gimr-logo.png"
org_info = ''

# Certificates
beacon_server_crt = ''
beacon_server_key = ''

# Query Budget
query_budget_per_user = False
query_budget_per_ip = False
query_budget_amount = 3
query_budget_time_in_seconds = 20
query_budget_database = 'mongo'
query_budget_db_name = 'beacon'
query_budget_table = 'budget'

# Query Rounding
imprecise_count=0 # If imprecise_count is 0, no modification of the count will be applied. If it's different than 0, count will always be this number when count is smaller than this number.
round_to_tens=False # If true, the rounding will be done to the immediate superior tenth if the imprecise_count is 0
round_to_hundreds=False # If true, the rounding will be done to the immediate superior hundredth if the imprecise_count is 0 and the round_to_tens is false
