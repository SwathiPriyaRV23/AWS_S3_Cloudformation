import json
filepath = "C:\\Users\\Administrator\\PycharmProjects\\S3\\test1.json"
AccessControl = input("Enter AccessControl : Private, PublicRead, PublicReadWrite, AuthenticatedRead, "
                      "LogDeliveryWrite, BucketOwnerRead, BucketOwnerFullControl, or AwsExecRead")
BucketName = input("Enter Bucket Name: ")
ObjectLockEnabled = input("Enter True or False for ObjectLockEnabled : ")
AccelerationStatus = input("Enter Enabled | Suspended for AccelerationStatus:")
BlockPublicAcls = input("Enter a Boolean value for BlockPublicAcls: ")
BlockPublicPolicy = input("Enter a Boolean value for BlockPublicPolicy: ")
IgnorePublicAcls = input("Enter a Boolean value for IgnorePublicAcls: ")
RestrictPublicBuckets = input("Enter a Boolean value for RestrictPublicBuckets: ")

data = { "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "AccessControl": AccessControl,
                "BucketName": BucketName ,
                "ObjectLockEnabled": ObjectLockEnabled,
                "AccelerateConfiguration": {
                      "AccelerationStatus": AccelerationStatus
                },
                "PublicAccessBlockConfiguration":{
                    "BlockPublicAcls": BlockPublicAcls ,
                    "BlockPublicPolicy": BlockPublicPolicy,
                    "IgnorePublicAcls": IgnorePublicAcls,
                    "RestrictPublicBuckets": RestrictPublicBuckets
                }
            }
        } } }



def nonull_dict(d):
    new_dict = {}
    for k, v in d.items():
        if isinstance(v,dict):
            v = nonull_dict(v)
        if not v in (u'', None, {}):
            new_dict[k] = v
    return new_dict

newdata = nonull_dict(data)


def json_dump(newdata, filepath):
 with open(filepath,"w") as descriptor:
    if (AccessControl in ("Private", "PublicRead", "PublicReadWrite", "AuthenticatedRead",
                      "LogDeliveryWrite", "BucketOwnerRead", "BucketOwnerFullControl", "AwsExecRead"))\
        and (type(BucketName) == str) and (ObjectLockEnabled in ('True','False'))and (AccelerationStatus in ('Enabled','Disabled')) \
        and (BlockPublicAcls in ('True','False')) and (BlockPublicPolicy in ('True','False')) and (IgnorePublicAcls in ('True','False')) \
        and (RestrictPublicBuckets in ('True','False')):
            json.dump(newdata, descriptor)
    elif (AccessControl == "") or (BucketName == "") or (ObjectLockEnabled == "") or (AccelerationStatus == "") or (BlockPublicAcls == "")\
            or (BlockPublicPolicy == "") or (IgnorePublicAcls == "") or (RestrictPublicBuckets == ""):
        print("Run the code again to enter values or skip this step to continue without null valued property in the output file")
        json.dump(newdata, descriptor)


json_dump(newdata, filepath)
