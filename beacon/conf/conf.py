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
beacon_id = 'org.garvan.rddp-beacon'  # ID of the Beacon
beacon_name = 'Garvan RDDP cohort-level beacon'  # Name of the Beacon service
api_version = 'v2.0.0' # Version of the Beacon implementation
uri = 'http://beaconprod:5050/api/'
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
cors_urls = ["http://localhost:3000","https://cancer-beacon-demo.ega-archive.org", "https://beacon-network-demo2.ega-archive.org", "https://beacon.ega-archive.org"]

# Service Info
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Organization info
org_id = 'Garvan'  # Id of the organization
org_name = 'Garvan Institute for Medical Research'  # Full name
org_description = 'Garvan Institute of Medical Research is one of Australia’s premier medical research institutes '
org_adress = '384 Victoria Street, Darlinghurst NSW 2010, Australia'
org_welcome_url = 'https://garvan.org.au'
org_contact_url = 'mailto:dsp@garvan.org.au'
org_logo_url = 'https://images.contentstack.io/v3/assets/blt324fd0a04af716e6/blt3f0048229394c515/6405de96205f2b7a60b745d6/gimr-logo.png'
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
