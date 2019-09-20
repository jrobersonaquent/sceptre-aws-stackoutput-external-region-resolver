# Stack Output External Region

This resolver fetches the value of an output from a different Stack in a different region. You can specify a optional
AWS profile to connect to a different account. It works the same way as `!stack_output_external` but with the added region parameter. This is so you can reference a stack in another region other than the region defined in the stack configuration. It also maintains the optional extra profile parameter that `!stack_output_external` has.

Here is a simple example use:

```yaml
# config/dev/us-east-1/example-io-zone.yaml
template_path: hosted-zone.yaml
profile: dev
parameters:
  Name: example.io
```
```yaml
# templates/hosted-zone.yaml
...

Outputs:
  HostedZoneID:
    Description: Hosted zone ID
    Value: !Ref HostedZone
```
```yaml
# config/dev/us-west-2/db-dns.yaml

region: us-west-2
profile: dev
parameters:
  HostedZoneID: !stack_output_external_region dev-us-east-1-example-com-zone::HostedZoneID us-east-1
```

Here is another example use with profile

```yaml
# config/internal/us-east-1/nessus-scanner.yaml
template_path: ec2-instance.yaml
profile: internal
parameters:
  ...
```
```yaml
# templates/ec2-instance.yaml
...

Outputs:
  InstanceId:
    Description: Instance ID
    Value: !Ref Instance
  PrivateIp:
    Description: Instance private IP
    Value: !GetAtt Instance.PrivateIp
  PublicIp:
    Description: Instance public IP (EIP)
    Value: !Ref ElasticIP
```
```yaml
# config/dev/us-west-2/app-server.yaml
template_path: ec2-instance.yaml
profile: prod
parameters:
  AllowAccess:
    - address: 0.0.0.0/0
      port: 80
    - address: !stack_group_external_region internal-us-east-1-nessus-scanner::PrivateIp internal
      port: 22
```
