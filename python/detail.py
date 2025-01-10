import json

def parse_transaction_data(data):
    json_data = json.loads(data)

    # 获取 slot
    slot = json_data.get("slot", 0)
    print(f"Slot: {slot}")

    # 获取签名
    signatures = json_data.get("transaction", {}).get("transaction", {}).get("signatures", [])
    print(f"Signatures: {signatures}")

    # 获取账户列表
    account_keys = json_data.get("transaction", {}).get("transaction", {}).get("message", {}).get("account_keys", [])
    account_pubkeys = [acc.get("pubkey", "") for acc in account_keys]
    print(f"Account Keys: {account_pubkeys}")

    # 获取指令
    instructions = json_data.get("transaction", {}).get("transaction", {}).get("message", {}).get("instructions", [])
    for idx, instruction in enumerate(instructions, start=1):
        print(f"Instruction {idx}: {instruction}")

if __name__ == "__main__":
    raw_data = '<你的 JSON 数据>'
    parse_transaction_data(raw_data)
