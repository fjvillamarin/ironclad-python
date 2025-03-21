# ListAllRecordsMetadata200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_types** | [**ListAllRecordsMetadata200ResponseRecordTypes**](ListAllRecordsMetadata200ResponseRecordTypes.md) |  | [optional] 
**properties** | [**ListAllRecordsMetadata200ResponseProperties**](ListAllRecordsMetadata200ResponseProperties.md) |  | [optional] 
**attachments** | [**ListAllRecordsMetadata200ResponseAttachments**](ListAllRecordsMetadata200ResponseAttachments.md) |  | [optional] 
**links** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.list_all_records_metadata200_response import ListAllRecordsMetadata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllRecordsMetadata200Response from a JSON string
list_all_records_metadata200_response_instance = ListAllRecordsMetadata200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllRecordsMetadata200Response.to_json())

# convert the object into a dict
list_all_records_metadata200_response_dict = list_all_records_metadata200_response_instance.to_dict()
# create an instance of ListAllRecordsMetadata200Response from a dict
list_all_records_metadata200_response_from_dict = ListAllRecordsMetadata200Response.from_dict(list_all_records_metadata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


