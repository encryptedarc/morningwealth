# Fundamental Source Policy

ใช้ policy นี้กับการวิเคราะห์คุณภาพธุรกิจและงบการเงิน การค้นเว็บเป็นวิธีหาเอกสาร ไม่ใช่ระดับความน่าเชื่อถือของข้อมูล

## Source hierarchy

ใช้แหล่งข้อมูลตามลำดับ authority:

1. **Regulatory filings and filed statements** — SEC EDGAR, SET/ก.ล.ต., exchange filings, 10-K, 10-Q, 20-F, 6-K, 8-K, 56-1 One Report และงบการเงินที่ยื่นต่อหน่วยงานกำกับ
2. **Audited company reports** — annual report, audited financial statements และ footnotes จากบริษัท
3. **Official earnings and management materials** — earnings release, earnings presentation, earnings call, investor day และ IR release ใช้กับ results, strategy, guidance และ management claims; earnings release อาจยังไม่ได้ audited จึงต้อง reconcile กับ filed statements เมื่อมี filing
4. **Independent secondary sources** — Reuters, Bloomberg, FT, WSJ, CNBC, Bangkok Post และสื่อการเงินที่น่าเชื่อถือ ใช้ยืนยันเหตุการณ์ภายนอกหรือเพิ่มบริบท
5. **Aggregators and quote pages** — Yahoo Finance, Google Finance, Settrade, TradingView และฐานข้อมูลสรุป ใช้เป็น last resort และต้องตรวจ timestamp/basis

WebSearch หรือ search snippet ช่วยค้นหา source เท่านั้น ห้ามอ้าง snippet แทน filing เมื่อเอกสารต้นทางเข้าถึงได้

ห้ามใช้ model memory, AI prediction sites, sponsored content ที่ไม่มี disclosure, forum หรือ social post ที่ไม่ยืนยันตัวตนเป็น fact

## Freshness by data type

### Live market data

ราคา, market cap, FX, yield และ current valuation multiples ต้องมาจากข้อมูลภายใน 24 ชั่วโมงหรือ expected close window พร้อม timestamp:

- `✅ FRESH` — close ล่าสุดหรือข้อมูลภายใน 24 ชั่วโมง
- `⚠️ INTRADAY` — ระหว่างตลาดเปิด
- `⚠️ PRE-MARKET / AFTER-HOURS` — extended-hours data
- ไม่มี timestamp หรือเก่ากว่า close ที่ควรมี — เขียน `ไม่มีข้อมูลอัปเดต`

### Filing and financial-statement data

งบไม่ใช้เกณฑ์ 24 ชั่วโมง ให้ถือว่า usable เมื่อ:

- เป็น annual/interim filing ล่าสุดที่บริษัทเผยแพร่ ณ วันที่ค้นข้อมูล
- ระบุ fiscal period และ filing/publication date
- ตรวจแล้วว่าไม่มี amended/restated filing ที่ใหม่กว่า
- basis ตรงกับการเปรียบเทียบ เช่น reported เทียบ reported และ quarter เทียบช่วงเดียวกันปีก่อน

ถ้ามี filing ที่ใหม่กว่าหรือ restatement ให้ฉบับเก่าถูก supersede ถ้าบริษัทควรรายงานงวดใหม่แล้วแต่ยังหาไม่ได้ ให้ระบุ data gap แทนการเดา

### Events after the reporting period

ตรวจ 8-K/6-K, SET disclosure, company announcement และข่าวที่เชื่อถือได้หลัง balance-sheet date แยกเหตุการณ์เหล่านี้ออกจากผลประกอบการของงวดเดิมอย่างชัดเจน

## Cross-verification

- ตัวเลขจาก filing โดยตรงไม่ต้องมี secondary source ซ้ำ หาก period, unit และ basis ตรงกัน
- ตรวจ totals, subtotals และ derived metrics ให้ reconcile กับงบและ footnotes
- ถ้า aggregator หรือ presentation ขัดกับ filing ให้ใช้ filing และอธิบายความต่าง
- ถ้า primary filings ขัดกัน ให้ใช้ amended/restated filing ล่าสุดและระบุการเปลี่ยนแปลง
- ราคาเปลี่ยน `|change| ≥ 3%`, gap หรือ unusual volume ต้องยืนยันด้วยแหล่งข้อมูลตลาดอีกหนึ่งแห่ง
- ถ้าความขัดแย้งของข้อมูล material ยัง resolve ไม่ได้ ให้แสดงทั้งสองค่าและหยุด verdict ในส่วนที่ได้รับผลกระทบ

## Citation and precision

- Sourced figure: `[Source, publication date, fiscal period]`
- Material factual claim: `[Source, publication date]` และเพิ่ม fiscal period เมื่อ claim ผูกกับงบหรือผลประกอบการ
- Live figure: `[Source, timestamp, market session]`
- Derived figure: แสดงสูตรและ input ที่อ้างอิงได้
- Management guidance: ระบุชัดว่าเป็น guidance/target ไม่ใช่ผลจริง
- ไม่มีข้อมูลที่ตรวจสอบได้: เขียนตรง ๆ ว่า `ไม่มีข้อมูลที่ตรวจสอบได้`

ตัวอย่าง:

```text
Revenue FY2025 $10.2B [Company 10-K, Feb 20 2026, FY ended Dec 31 2025]
FCF $1.1B = CFO $1.6B - capex $0.5B [Company 10-K, Feb 20 2026, FY2025]
Management targets gross margin above 60% [Q2 earnings call, Aug 7 2026] — Management guidance
```

ห้ามใช้ `~`, `ประมาณ`, `around` หรือค่าที่จำจาก model แทน sourced figures

## Pre-output check

1. บริษัท, ticker และ exchange ถูกต้องหรือไม่
2. Annual และ interim filing เป็นฉบับล่าสุดที่หาได้หรือไม่
3. ทุก sourced number/claim มี source + publication date หรือ timestamp ตามประเภท และ fiscal period เมื่อ applicable หรือไม่
4. Live market data อยู่ใน freshness window และมี timestamp หรือไม่
5. Reported/adjusted, consolidated/segment และ currency/unit ตรงกันหรือไม่
6. Derived figures แสดงสูตรและ reconcile ได้หรือไม่
7. Management claims และ analytical inference ถูกแยกจาก facts หรือไม่

ถ้าข้อใดตอบไม่ได้ ให้ค้นเพิ่มหรือระบุ data gap ห้ามเติมค่าด้วยการคาดเดา
