# Auto Video Uploader 🎥

## الوصف
مشروع بسيط ينشئ فيديو تلقائيًا من نص، يضيف صوت، ومن ثم يرفعه على YouTube بشكل يومي.

## المتطلبات
- إعداد YouTube API credentials وOAuth refresh token
- إنشاء `secrets` في GitHub:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `REFRESH_TOKEN`
  - `CHANNEL_ID` (اختياري)

## كيفية الاستخدام
1. أنشئ repo جديد على GitHub واسميه `auto-video-uploader`.
2. أنشئ المجلدات والملفات كما هو موضح أعلاه.
3. انسخ الأكواد في الملفات المناسبة.
4. ارفع المشروع على GitHub.
5. أضف `secrets` المذكورة.
6. GitHub Actions سيعمل تلقائيًا كل يوم أو عند كل push.

## 👍 جاهز للتجربة
بعد رفع الأكواد وإضافة secrets، تابع صفحة Actions في GitHub وانتظر تشغيل workflow.  
إذا ظهرت أخطاء، ابعث لي الرسالة وأنا معك لحلها 💪
