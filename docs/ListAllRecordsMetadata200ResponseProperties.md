# ListAllRecordsMetadata200ResponseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_notes** | [**ListAllRecordsMetadata200ResponsePropertiesAdditionalNotes**](ListAllRecordsMetadata200ResponsePropertiesAdditionalNotes.md) |  | [optional] 
**agreement_date** | [**ListAllRecordsMetadata200ResponsePropertiesAgreementDate**](ListAllRecordsMetadata200ResponsePropertiesAgreementDate.md) |  | [optional] 
**workflow_id** | [**ListAllRecordsMetadata200ResponsePropertiesWorkflowId**](ListAllRecordsMetadata200ResponsePropertiesWorkflowId.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_records_metadata200_response_properties import ListAllRecordsMetadata200ResponseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllRecordsMetadata200ResponseProperties from a JSON string
list_all_records_metadata200_response_properties_instance = ListAllRecordsMetadata200ResponseProperties.from_json(json)
# print the JSON string representation of the object
print(ListAllRecordsMetadata200ResponseProperties.to_json())

# convert the object into a dict
list_all_records_metadata200_response_properties_dict = list_all_records_metadata200_response_properties_instance.to_dict()
# create an instance of ListAllRecordsMetadata200ResponseProperties from a dict
list_all_records_metadata200_response_properties_from_dict = ListAllRecordsMetadata200ResponseProperties.from_dict(list_all_records_metadata200_response_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


