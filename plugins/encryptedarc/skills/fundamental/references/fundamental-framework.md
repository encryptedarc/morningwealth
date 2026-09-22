# Fundamental Analysis Framework

ใช้ reference นี้หลัง resolve บริษัทและก่อนเริ่มวิเคราะห์ เลือกเฉพาะ metric ที่เหมาะกับ archetype; ไม่ต้องยัดทุกหัวข้อหากบริษัทไม่เปิดเผยข้อมูลหรือ metric ไม่มีความหมาย

## 1. Archetype and metric selection

| Archetype | Metric ที่ควรเน้น | Metric ที่ต้องระวังหรือไม่ควรใช้เดี่ยว ๆ |
|---|---|---|
| General corporate | revenue growth, gross/operating margin, CFO, FCF, ROIC, net debt/EBITDA, interest coverage | net income ที่มี one-off, EBITDA ที่ไม่หัก recurring capex |
| Bank | loan/deposit growth, NIM, fee income, NPL ratio, coverage ratio, credit cost, CET1/CAR, ROE | FCF, net debt/EBITDA, EV/EBITDA |
| Insurer | premium growth, underwriting result, combined ratio, solvency ratio, investment income, ROE | revenue growth หรือ P/E โดยไม่แยก underwriting cycle |
| REIT/property fund | occupancy, rental reversion, WALE, NOI, FFO/AFFO, DPU, gearing, interest coverage | EPS, net income และ P/E ที่ถูก distortion จาก depreciation/fair-value changes |
| Cyclical/commodity | volume, realized price, unit cost, utilization, balance sheet through cycle, normalized earnings | trailing P/E ที่จุด peak/trough ของ cycle |
| SaaS/subscription | ARR, recurring mix, NRR/churn, gross margin, sales efficiency, FCF, SBC และ dilution | adjusted EBITDA ที่ตัด SBC แต่ไม่พูดถึง dilution |
| Pre-profit/high-growth | runway, cash burn, gross margin trajectory, unit economics, dilution, path to breakeven | ROE/ROIC และ point forecast ที่ยังไม่มี operating history |

Hybrid company ใช้หลาย archetypeได้ แต่ต้องบอกว่าแต่ละส่วนใช้กรอบใด

## 2. Required output structure

### 1) Company Snapshot and Data as of

- ชื่อบริษัท, ticker, exchange และ fiscal year-end
- วันที่ค้นข้อมูล งวด annual ล่าสุด และงวด interim ล่าสุด
- อธิบายบริษัทหนึ่งประโยคด้วยภาษาคนทั่วไป
- ระบุ source ที่หาไม่ได้หรือ stale ตั้งแต่ต้น

### 2) ธุรกิจ ลูกค้า และโมเดลรายได้

- สินค้า/บริการและวิธีหาเงิน
- revenue segments พร้อมสัดส่วนจากงวดที่อ้างถึง
- ลูกค้าหลัก, geography, channel และ customer concentration ถ้ามี disclosure
- recurring vs transactional revenue, pricing model และ switching behavior
- ระบุว่า growth มาจาก volume, price, mix, acquisition หรือ accounting effect

### 3) Financial Trend

ทำตาราง annual 3 ปีล่าสุดและ quarter/interim ล่าสุดเทียบ YoY เท่าที่มีข้อมูล โดยเลือก metric ให้ตรง archetype ตารางต้องระบุ currency/unit และ period

สำหรับบริษัททั่วไปควรพิจารณา:

- revenue, gross profit/margin, operating profit/margin และ net income
- CFO, capex และ FCF โดยนิยาม default `FCF = CFO - capex`
- cash, gross debt, net debt และดอกเบี้ย
- diluted shares; ตรวจ buyback, issuance และ SBC dilution

ห้ามเปรียบเทียบ quarter กับ full year หรือ reported กับ adjusted โดยไม่อธิบาย reconciliation

### 4) คุณภาพกำไร งบ และ Cash Conversion

ตรวจอย่างน้อย:

- กำไรโตตามรายได้หรือเกิดจาก one-off, tax, FX หรือ fair-value gain
- CFO และ FCF สอดคล้องกับกำไรหรือไม่
- receivables, inventory และ contract assets โตเร็วกว่ารายได้หรือไม่
- capex เป็น maintenance หรือ growth เท่าที่ disclosure แยกได้
- debt maturity, refinancing need และ interest coverage
- ROIC/ROE/ROA ใช้ metric ใดจึงเหมาะกับ archetype และเหตุใด

### 5) Moat and Growth Optionality

Moat ต้องมี observable evidence เช่น margin durability, pricing power, retention, market share, cost position, network density, regulatory license หรือ ROIC ที่สูงกว่าต้นทุนเงินทุนหลายงวด ห้ามใช้ brand/technology/network effect เป็น moat เพียงเพราะผู้บริหารเรียกเช่นนั้น

แยก growth option เป็นสามระดับ:

- `ในงบแล้ว` — มีรายได้ ลูกค้า หรือ capacity contribution ที่ตรวจสอบได้
- `กำลังพิสูจน์` — มี product launch, contract, capex หรือ KPI แต่ยังไม่ material
- `ยังเป็นความหวัง` — มีเพียงเป้าหมายหรือ narrative

### 6) Management and Capital Allocation

- เทียบ guidance/KPI ที่ผู้บริหารเคยให้กับผลจริงย้อนหลังเมื่อมีข้อมูล
- ตรวจ acquisition, divestment, capex, dividend, buyback, debt paydown และ equity issuance
- แยก execution evidence ออกจากบุคลิกหรือคำพูดใน earnings call
- ถ้าไม่มี guidance history เพียงพอ ให้เขียน `ยังประเมินความแม่นของ guidance ไม่ได้`

### 7) Risks, Red Flags, and What I Don't Know

จัดอันดับ 3-5 risks ตาม `Impact` และ `Likelihood` พร้อม leading indicator ที่ควรติดตาม ครอบคลุมเฉพาะที่ material เช่น competition, customer concentration, regulation, cyclicality, margin pressure, leverage, dilution, accounting quality และ valuation risk

`What I Don't Know` ต้องระบุ data gap และบอกว่าจะตรวจต่อจาก filing, footnote, IR page หรือ transcript ใด

### 8) Scorecard and Final Verdict

ให้คะแนนเฉพาะหัวข้อที่มีหลักฐาน:

| หัวข้อ | สิ่งที่ประเมิน |
|---|---|
| ความเข้าใจง่ายของธุรกิจ | revenue driver และ economics อธิบายได้ชัดหรือไม่ |
| คุณภาพรายได้ | recurring, diversification, pricing power และ visibility |
| คุณภาพกำไรและ cash conversion | earnings แปลงเป็นเงินสดและไม่มี distortion มากเกินไป |
| ความแข็งแรงของงบ | liquidity, leverage, maturity และ resilience |
| ความสามารถในการเติบโต | runway, reinvestment opportunity และ execution evidence |
| ความได้เปรียบเชิงแข่งขัน | moat ที่มีหลักฐานและความคงทน |
| คุณภาพการจัดสรรเงินทุน | ผลของ capex, M&A, buyback, dividend และ dilution |
| ความทนทานต่อความเสี่ยง | 10 หมายถึงรับแรงกระแทกได้ดีและมี downside protection สูง |
| คุณภาพธุรกิจโดยรวม | สรุป business quality โดยไม่รวมความถูก/แพงของราคาหุ้น |

## 3. Scoring rubric

- `1-3` — อ่อนแอหรือมี red flag ที่พิสูจน์ได้
- `4-6` — ผสม มีข้อดีแต่ข้อจำกัดยัง material
- `7-8` — แข็งแรงและมีหลักฐานรองรับหลายงวด
- `9-10` — โดดเด่น พิสูจน์ได้ข้าม cycle หรือเหนือ peer อย่างสม่ำเสมอ
- `N/A` — ข้อมูลไม่พอหรือ metric ไม่เหมาะกับ archetype

ทุกคะแนนต้องมีเหตุผลหนึ่งบรรทัดและ citation ที่รองรับ ห้ามคำนวณคะแนนรวมด้วยค่าเฉลี่ยหากมีหัวข้อเป็น `N/A` หรือ archetype ทำให้น้ำหนักแต่ละ metric ไม่เท่ากัน

## 4. Final Verdict format

ปิดท้ายสั้นและตรง:

1. ธุรกิจนี้คืออะไรในภาษาคนทั่วไป
2. จุดแข็ง 3 ข้อ
3. จุดเสี่ยง 3 ข้อ
4. เหมาะกับการศึกษาของนักลงทุนลักษณะใด โดยไม่แนะนำให้ซื้อหรือขาย
5. Verdict: `พื้นฐานแข็งแรง`, `พื้นฐานดีแต่มีจุดต้องระวัง`, `พื้นฐานยังไม่แข็งแรง` หรือ `ข้อมูลไม่พอประเมิน`
6. ก่อนพิจารณาลงทุนควรตรวจเอกสารหรือ KPI ใดต่อ
