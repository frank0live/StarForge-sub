# StarForge PRO — صفحه اشتراک

یه صفحه‌ی استاتیک تک‌فایل، تیره و شیشه‌ای، کاملاً فارسی و راست‌چین — برای اینکه
کاربر لینک اشتراکش رو ببینه، کپی کنه، QR بگیره و با یه tap بندازه توی اپ.

This is a static single-page subscription viewer: open it with `?sub=<url>`,
or paste the subscription content manually. No backend, GitHub Pages ready.

## راه‌اندازی سریع

| کار | چطور |
|---|---|
| پیش‌نمایش لوکال | `python3 -m http.server` توی همین پوشه، بعد باز کردن `index.html` |
| حالت دمو | همین‌طوری بازش کن، داده نمایشی می‌بینی |
| اشتراک واقعی | `index.html?sub=https://…` — اگه سرور CORS نده، محتوا رو توی کادر بچسبون |
| انتشار | پوش به برنچ `main` → ورک‌فلوی Pages خودش منتشر می‌کنه |

## ساختار

| فایل | نقش |
|---|---|
| `index.html` | کل صفحه (استایل + منطق داخل خودش) |
| `assets/logo.svg` | لوگوی اوریجینال سندان فضایی + ستاره |
| `assets/demo-sub.txt` | نمونه اشتراک base64 برای دکمه «دمو» |
| `data/config.json` | متای برند و لیست اپ‌ها |
| `scripts/style_audit.py` | چک‌لیست ضد نشت برند (`python3 scripts/style_audit.py`) |
| `docs/` | جای اسکرین‌شات‌ها (فعلاً placeholder) |

## نکته مهم درباره CORS

سرور اشتراک هدر CORS نمی‌دهد، پس `fetch` مستقیم از مرورگر معمولاً fail می‌شود.
صفحه برای همین دو راه دارد: باز کردن از همان دامنه پنل (same-origin)، یا
چسباندن دستی محتوا در کادر. هر دو تست شده در منطق صفحه.

## پشتیبانی

https://t.me/master_supports

## Credits

Inspired by the classic bento-style subscription panel layout — this page is an
original implementation (own code, own logo, own styles), not a copy.

## License

MIT © 2026 frank0live — see `LICENSE`.
