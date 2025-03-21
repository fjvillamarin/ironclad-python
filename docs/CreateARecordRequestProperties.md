# CreateARecordRequestProperties

Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_date** | [**CreateARecordRequestPropertiesAgreementDate**](CreateARecordRequestPropertiesAgreementDate.md) |  | [optional] 
**counterparty_name** | [**CreateARecordRequestPropertiesCounterpartyName**](CreateARecordRequestPropertiesCounterpartyName.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_a_record_request_properties import CreateARecordRequestProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CreateARecordRequestProperties from a JSON string
create_a_record_request_properties_instance = CreateARecordRequestProperties.from_json(json)
# print the JSON string representation of the object
print(CreateARecordRequestProperties.to_json())

# convert the object into a dict
create_a_record_request_properties_dict = create_a_record_request_properties_instance.to_dict()
# create an instance of CreateARecordRequestProperties from a dict
create_a_record_request_properties_from_dict = CreateARecordRequestProperties.from_dict(create_a_record_request_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


