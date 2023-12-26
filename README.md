# starknet.py Feature Request
Parsing ABIs using AbiParser (any version) can be time-consuming; for example, processing the Argent ABI on an M1 Pro takes about 0.96 seconds. For use cases that require quick parsing, this can pose a performance bottleneck.

I am requesting an enhancement to the ABI parsing speed to cater to performance-critical applications.

To reproduce:

```
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
