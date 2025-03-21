# UpdateRecordMetadataRequestAddProperties

A key:value map of properties to add. The two below are examples.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | [**UpdateRecordMetadataRequestAddPropertiesCounterpartyName**](UpdateRecordMetadataRequestAddPropertiesCounterpartyName.md) |  | [optional] 
**agreement_date** | [**UpdateRecordMetadataRequestAddPropertiesAgreementDate**](UpdateRecordMetadataRequestAddPropertiesAgreementDate.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_record_metadata_request_add_properties import UpdateRecordMetadataRequestAddProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordMetadataRequestAddProperties from a JSON string
update_record_metadata_request_add_properties_instance = UpdateRecordMetadataRequestAddProperties.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordMetadataRequestAddProperties.to_json())

# convert the object into a dict
update_record_metadata_request_add_properties_dict = update_record_metadata_request_add_properties_instance.to_dict()
# create an instance of UpdateRecordMetadataRequestAddProperties from a dict
update_record_metadata_request_add_properties_from_dict = UpdateRecordMetadataRequestAddProperties.from_dict(update_record_metadata_request_add_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


