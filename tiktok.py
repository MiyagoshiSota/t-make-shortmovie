from TikTokApi import TikTokApi
import asyncio
import os

filename = "./tiktok_fashion_en.txt"

verifyFp = 'verify_lxl6yxp6_Nm1u4Hbw_TdPF_4Lna_Bkhs_CozREB4IEtnC'
msToken = '7Pstz-s9Cypy-KFcKwDlzkX_OOOtKHDYalvCP8zY8KwJKqlveqzHH7f8RosW-DJH_Fdqy0q0gxvj1itZvpOCPVvnEhvIFZG1RY6Rbct3-jM_5QsuIJyQ3PRQ3q2qGBlUCtToQISYz1NXxJ73S7uJ4bs='
ms_token = os.environ.get("ms_token", msToken)


async def get_hashtag_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token],
                                  num_sessions=1,
                                  sleep_after=3,
                                  headless=False)
        tag = api.hashtag(name="英語勉強")
        f = open(filename, 'w')
        async for video in tag.videos(count=100):
            videoinfo = video.as_dict
            f.writelines(videoinfo['desc'] + '\n\n')
            print([videoinfo['desc'], videoinfo['stats']])
        f.close()


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())
