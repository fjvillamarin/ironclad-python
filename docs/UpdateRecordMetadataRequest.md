# UpdateRecordMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of Record. | [optional] 
**name** | **str** | The name of the Record. | [optional] 
**add_properties** | [**UpdateRecordMetadataRequestAddProperties**](UpdateRecordMetadataRequestAddProperties.md) |  | [optional] 
**remove_properties** | **List[str]** | List of record property ids to be removed (e.g., [&#39;counterpartyAddress&#39;, &#39;agreementExpirationDate&#39;]) | [optional] 
**add_links** | [**List[RecordPropertyLinkModel]**](RecordPropertyLinkModel.md) | List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api). | [optional] 
**remove_links** | [**List[RecordPropertyLinkModel]**](RecordPropertyLinkModel.md) | List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api). | [optional] 
**set_parent** | [**CreateARecordRequestParent**](CreateARecordRequestParent.md) |  | [optional] 
**add_children** | [**List[RecordPropertyLinkModel]**](RecordPropertyLinkModel.md) | List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record. | [optional] 
**remove_parent** | **bool** | Boolean flag to indicate if the parent id should be removed for the current record. | [optional] 
**remove_children** | [**List[RecordPropertyLinkModel]**](RecordPropertyLinkModel.md) | List of objects containing the Record IDs or Ironclad IDs of the child records to be removed from the current record. | [optional] 

## Example

```python
from openapi_client.models.update_record_metadata_request import UpdateRecordMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordMetadataRequest from a JSON string
update_record_metadata_request_instance = UpdateRecordMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordMetadataRequest.to_json())

# convert the object into a dict
update_record_metadata_request_dict = update_record_metadata_request_instance.to_dict()
# create an instance of UpdateRecordMetadataRequest from a dict
update_record_metadata_request_from_dict = UpdateRecordMetadataRequest.from_dict(update_record_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


