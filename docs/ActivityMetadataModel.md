# ActivityMetadataModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**marked_up_message** | **str** |  | [optional] 
**added_participants** | [**List[UserModel]**](UserModel.md) |  | [optional] 
**replied_to** | [**CommentMetadataModelRepliedTo**](CommentMetadataModelRepliedTo.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_metadata_model import ActivityMetadataModel

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityMetadataModel from a JSON string
activity_metadata_model_instance = ActivityMetadataModel.from_json(json)
# print the JSON string representation of the object
print(ActivityMetadataModel.to_json())

# convert the object into a dict
activity_metadata_model_dict = activity_metadata_model_instance.to_dict()
# create an instance of ActivityMetadataModel from a dict
activity_metadata_model_from_dict = ActivityMetadataModel.from_dict(activity_metadata_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


