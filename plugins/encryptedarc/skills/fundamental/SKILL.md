---
name: fundamental
description: "Analyze a listed company's business quality and financial fundamentals in beginner-friendly Thai using primary filings and current company disclosures. Use for Fundamental analysis, พื้นฐานหุ้น, บริษัททำธุรกิจอะไร, งบแข็งแรงไหม, moat, revenue quality, or a beginner company primer. Do not use for price-only/news-only requests, short-term trading, portfolio allocation, or fair value/target-price work; use valuation-deep-dive for valuation."
---

# Fundamental

วิเคราะห์คุณภาพธุรกิจและฐานะการเงินของบริษัทจดทะเบียนสำหรับผู้เริ่มต้น โดยอธิบายเป็นภาษาไทยที่อ่านง่ายและมีหลักฐานตรวจสอบย้อนกลับได้ เป้าหมายคือช่วยให้ผู้ใช้เข้าใจว่า “บริษัทหาเงินอย่างไร พื้นฐานแข็งแรงแค่ไหน และต้องตรวจสอบอะไรต่อ” ไม่ใช่ออกคำแนะนำซื้อขาย

## Load before research

1. อ่าน `references/source-policy.md` เพื่อใช้ source hierarchy, freshness rules, citation และ cross-verification ที่แยก filing data ออกจาก live market data
2. อ่าน `references/fundamental-framework.md` เพื่อเลือก metric ตามประเภทธุรกิจ ใช้ output structure และ scorecard rubric

## Scope boundaries

- ใช้ skill นี้กับ business model, customers, revenue quality, financial health, moat, growth options, management execution, capital allocation และ fundamental risks
- อย่าใช้กับคำขอที่เน้นข่าว, catalysts, price action, macro หรือ short-term trading thesis
- ถ้าคำขอถาม fair value, target price, ถูกหรือแพง, DCF หรือ valuation method ให้ใช้ `valuation-deep-dive`
- พูดถึง valuation context ได้เฉพาะเมื่อจำเป็นต่อการอธิบาย risk และมีข้อมูลสดที่อ้างอิงได้ ห้ามสรุป fair value หรือจังหวะซื้อจาก skill นี้

## Workflow

### 1. Resolve the company

ระบุวันที่ปัจจุบันก่อนเริ่ม และยืนยันชื่อบริษัท, ticker และ exchange ให้ตรงกัน ถ้าชื่อกำกวมหรือ ticker ซ้ำหลายตลาด ให้ถามหนึ่งคำถามก่อนค้นข้อมูล

Default เมื่อผู้ใช้ไม่ระบุ:

- horizon ของข้อมูล: annual 3 ปีล่าสุด + quarter/interim ล่าสุดเทียบ YoY
- output: chat markdown
- audience: ผู้เริ่มต้นที่ต้องการเข้าใจพื้นฐาน ไม่ใช่ trade setup

### 2. Classify before choosing metrics

จัดบริษัทเป็นอย่างน้อยหนึ่ง archetype ก่อนวิเคราะห์: general corporate, bank, insurer, REIT/property fund, cyclical/commodity, SaaS/subscription หรือ pre-profit/high-growth แล้วใช้เฉพาะ metric ที่เหมาะจาก `references/fundamental-framework.md`

ห้ามฝืนใช้ FCF, ROIC, debt หรือ P/E แบบเดียวกับทุกธุรกิจ ถ้า metric ไม่เหมาะ ให้ข้ามและบอกเหตุผลสั้น ๆ

### 3. Research primary sources first

ใช้ลำดับหลักฐานดังนี้:

1. Latest annual filing: 10-K, 20-F, annual report หรือ 56-1 One Report
2. Latest quarterly/interim filing: 10-Q, 6-K, financial statements และ MD&A
3. Earnings presentation และ earnings call สำหรับ guidance, strategy และ management claims
4. Company IR disclosures และข่าวที่ตรวจสอบได้สำหรับเหตุการณ์หลังงบ

Investor presentation และ earnings call เป็นคำกล่าวของผู้บริหาร ไม่ใช่หลักฐานอิสระ ตรวจสอบ headline numbers กับงบหรือ filing ก่อนใช้ ถ้า transcript, segment data หรือ customer concentration ไม่มี ให้ระบุว่าไม่มีข้อมูลที่ตรวจสอบได้

### 4. Keep the evidence register explicit

- ทุกตัวเลขและ material factual claim ต้องมี source + publication date; เพิ่ม fiscal period เมื่อ claim ผูกกับงบหรือผลประกอบการ
- ระบุสกุลเงิน หน่วย และ basis ให้ชัด เช่น reported/adjusted, consolidated/segment, annual/quarterly
- ถ้าคำนวณเอง ให้แสดงสูตรและแยก derived figure ออกจาก sourced figure
- แยก `Fact`, `Management claim` และ `Analysis/Inference` ออกจากกัน
- ห้ามเขียนว่าตลาด “ยังไม่ price in” optionality หากไม่มี valuation evidence รองรับ ให้ใช้ว่า “ยังไม่ material ในงบ” หรือ “ยังเป็น management target” ตามหลักฐาน
- ถ้าข้อมูลไม่พอ ห้ามให้คะแนนด้วยการเดา ให้ใช้ `N/A — ข้อมูลไม่เพียงพอ`

### 5. Analyze, then deliver

ใช้โครงสร้าง 8 ส่วนใน `references/fundamental-framework.md` ตัดหัวข้อที่ไม่มีสาระสำคัญออกได้ แต่ต้องมี Data as of, Financial Trend, Risks, Scorecard, What I Don't Know และ Final Verdict

อธิบายศัพท์เฉพาะเมื่อปรากฏครั้งแรกด้วยภาษาง่ายในวงเล็บ ใช้ technical terms สากล เช่น revenue, margin, FCF, ROIC, NIM และ AFFO ตามปกติ

## Verdict rules

เลือก verdict ตามหลักฐานหนึ่งรายการ:

- `พื้นฐานแข็งแรง`
- `พื้นฐานดีแต่มีจุดต้องระวัง`
- `พื้นฐานยังไม่แข็งแรง`
- `ข้อมูลไม่พอประเมิน`

Verdict ต้องแยก “คุณภาพบริษัท” ออกจาก “ความน่าสนใจของราคาหุ้น” บริษัทดีอาจเป็นหุ้นที่แพง และหุ้นราคาถูกอาจเป็นธุรกิจที่อ่อนแอ

ปิดท้ายทุกครั้งด้วย:

> ข้อมูลนี้เพื่อการศึกษา ไม่ใช่คำแนะนำการลงทุน — กรุณาปรึกษา licensed advisor ก่อนตัดสินใจ
