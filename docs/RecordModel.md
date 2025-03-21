# RecordModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ironclad_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**properties** | [**RecordModelProperties**](RecordModelProperties.md) |  | [optional] 
**attachments** | [**RecordModelAttachments**](RecordModelAttachments.md) |  | [optional] 
**links** | [**List[RecordModelLinksInner]**](RecordModelLinksInner.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**child_ids** | **List[str]** |  | [optional] 
**source** | [**RecordModelSource**](RecordModelSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_model import RecordModel

# TODO update the JSON string below
json = "{}"
# create an instance of RecordModel from a JSON string
record_model_instance = RecordModel.from_json(json)
# print the JSON string representation of the object
print(RecordModel.to_json())

# convert the object into a dict
record_model_dict = record_model_instance.to_dict()
# create an instance of RecordModel from a dict
record_model_from_dict = RecordModel.from_dict(record_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


