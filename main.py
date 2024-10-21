from apis.clients.tm_api_client import tm_v1_client, tm_v2_client
from json import dumps


async def main():
    response = tm_v1_client.get_full_export_preview()
    fields_format = response['format']
    items = response['items']
    i = 0
    for item in items:
        if i == 1:
            break
        res = await tm_v1_client.get_full_export_by_json(item)
        i += 1
        print(dumps(res, indent=4))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

    