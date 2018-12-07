To generate the gRPC stubs execute `make build` or 

```bash
python -m grpc_tools.protoc --proto_path=./proto --python_out=. --grpc_python_out=. ./proto/digestor/digestor.proto
```

To test:

```
In [1]: from digestor.client import DigestorClient

In [2]: client = DigestorClient()

In [3]: client.get_digest('My name is Adam!')
Out[4]: Digest: "cba6438f175113defc680de998f96481330928570d7e1326422d912dda2ab8a2"
```

### Source

https://technokeeda.com/programming/grpc-python-tutorial/