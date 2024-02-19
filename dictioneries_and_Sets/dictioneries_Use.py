ec2_instance_info = [
    {
        'id':'instance-001',
        'type': 't2.micro'
    },
    {
        'id':'instance-002',
        'type': 't2.nano'
    },
    {
        'id':'instance-003',
        'type': 't2.medium'
    },
    {
        'id':'instance-004',
        'type': 't2.small'
    }
]
print(ec2_instance_info[1]['type'])