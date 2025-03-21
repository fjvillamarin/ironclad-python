# EmailNotFound

Email ID Not Found Request Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_not_found import EmailNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotFound from a JSON string
email_not_found_instance = EmailNotFound.from_json(json)
# print the JSON string representation of the object
print(EmailNotFound.to_json())

# convert the object into a dict
email_not_found_dict = email_not_found_instance.to_dict()
# create an instance of EmailNotFound from a dict
email_not_found_from_dict = EmailNotFound.from_dict(email_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


