---
title: "Telechips Android 14 IVI SDK v1.1.0 Release"
description: "SDK release notes and instructions for TCC807x and TCC805x EVBs"
---

import { Alert } from "@/components/Alert"
import { CodeBlock } from "@/components/CodeBlock"

# 🚀 Telechips Android 14 IVI SDK v1.1.0 Release

<Alert type="warning">
  ⚠️ **Important Notice**  
  This SDK has known limitations. Please refer to the relevant <strong>Release Notes</strong> for detailed information.
</Alert>

- Source code and binaries for sub-core are included.  
- This version is configured to download AOSP sources directly from the official Google server.  
- Telechips-specific AOSP fixes are separated into a dedicated patch folder.  
  - See <strong>Chapter 4.1.2.1</strong> in the <em>Getting Started Guide</em> (Android 14 SDK for TCC807x and TCC805x).

---

## 📥 Download Instructions

<CodeBlock language="bash">
{`
$ repo init -u ssh://rgit.telechips.com/android/android14_ivi/1.1.0/platform/manifest -b android14_ivi_1.1.0 -m default.xml
$ repo sync
`}
</CodeBlock>

---

## 🔧 Supported Products

- **TCC8070(CS) EVB**
- **TCC8050 / TCC8053 / TCC8059 EVB**

---

## 📚 Reference Documents

### 📌 TCC8070

- <a href="#">Android 14 IVI SDK - Getting Started for TCC807x v1.30[A].pdf</a>
- <a href="#">Android 14 IVI SDK - How to Calculate PMAP for TCC807x v1.10[A].xlsx</a>
- <a href="#">Android 14 IVI SDK - Benchmark Result for TCC807x v1.10[A].pdf</a>
- <a href="#">Android 14 IVI SDK - Release Note for TCC807x v1.1.0[A].pdf</a>

### 📌 TCC805x

- <a href="#">Android 14 IVI SDK - Getting Started for TCC805x v1.20[A].pdf</a>
- <a href="#">Android 14 IVI SDK - How to Calculate PMAP for TCC805x v1.10[A].xlsx</a>
- <a href="#">Android 14 IVI SDK - Benchmark Result for TCC805x v1.10[A].pdf</a>
- <a href="#">Android 14 IVI SDK - Release Note for TCC805x v1.1.0[A].pdf</a>

---

## ❓ Troubleshooting

<Alert type="info">
  ✅ <strong>Access Denied?</strong><br />
  Please contact <a href="mailto:sales@telechips.com">sales@telechips.com</a>
</Alert>

