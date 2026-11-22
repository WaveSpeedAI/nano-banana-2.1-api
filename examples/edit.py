"""Nano Banana 2.1 — image-to-image with `google/nano-banana-2.1/edit`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import nano_banana_api

urls = nano_banana_api.edit(
    prompt="Describe the result you want",
    images=["https://example.com/your-image.jpg"],
)
print(urls[0])
