# Data dictionary — `ppp_ct.csv`

**OPIM 5641 · Studio 1 · PPP loans in Connecticut**

117,888 Paycheck Protection Program loans made to Connecticut businesses in 2020–21, from the
[SBA's public FOIA release](https://data.sba.gov/dataset/ppp-foia) (September 2024 vintage), filtered to
`BorrowerState == "CT"`. All 53 published columns are intact — including the messy ones. Descriptions
below are from the [official SBA dictionary](https://data.sba.gov/sites/default/files/distribution/SBA-OCA-2022-07-001/ppp-data-dictionary.xlsx),
with course notes in *italics*.

## The columns you'll use most tonight

| Column | What it is | Watch out |
|---|---|---|
| `LoanNumber` | Unique loan identifier | *Use this (not `BorrowerName`) to check for duplicates — many businesses legitimately appear twice (first + second draw).* |
| `BorrowerName` | Business name | *Same employer can be spelled differently across rows.* |
| `BorrowerCity` | Borrower city | *Dirty: "WEST HARTFORD", "West Hartford", "W HARTFORD" are all real values. `.str.upper().str.strip()` helps but doesn't fix everything.* |
| `InitialApprovalAmount` | Loan approval amount at origination ($) | *Wildly right-skewed — mean ≫ median. Log-scale bins or you'll see nothing.* |
| `CurrentApprovalAmount` | Loan approval amount, current ($) | *Differs from initial when a loan was increased/reduced after origination.* |
| `ForgivenessAmount` | Amount forgiven ($) | *Missing ≠ zero: blank can mean "not forgiven" or "no forgiveness reported."* |
| `JobsReported` | Number of employees | *Self-reported at application. Zeros, blanks, and implausible values are part of the story — interrogate before you trust dollars-per-job.* |
| `NAICSCode` | 6-digit NAICS industry code | *First 2 digits = sector. Missing for a chunk of rows — count what you drop.* |
| `DateApproved` | Loan funded date | *String; parse with `pd.to_datetime`. Two waves visible: spring 2020 and early 2021.* |
| `BusinessType` | Business type description | *Sole Proprietorship, LLC, Non-Profit, etc.* |

## Loan mechanics

| Column | What it is |
|---|---|
| `ProcessingMethod` | `PPP` = first-draw loan; `PPS` = second-draw loan |
| `Term` | Loan maturity, in months |
| `SBAGuarantyPercentage` | SBA guaranty percentage (100 for PPP) |
| `UndisbursedAmount` | Amount approved but not disbursed |
| `LoanStatus` | Status description — *"Exemption 4" means the loan is disbursed but not yet Paid in Full or Charged Off (FOIA redaction, not a real status)* |
| `LoanStatusDate` | Date of that status — *blank under the same Exemption-4 condition* |
| `ForgivenessDate` | Date forgiveness was paid |

## Who and where

| Column | What it is |
|---|---|
| `BorrowerAddress` / `BorrowerState` / `BorrowerZip` | Borrower street address, state (all "CT" here), ZIP |
| `ProjectCity` / `ProjectCountyName` / `ProjectState` / `ProjectZip` | Where the money was used (usually = borrower location) |
| `CD` | Project congressional district |
| `RuralUrbanIndicator` | `R`ural / `U`rban |
| `HubzoneIndicator` | In a HUBZone (historically underutilized business zone), Y/N |
| `LMIIndicator` | Low-and-moderate-income area, Y/N |
| `BusinessAgeDescription` | e.g., "Existing or more than 2 years old", "Startup" |
| `FranchiseName` | Franchise name, if any (mostly blank) |
| `NonProfit` | "Yes" if the business type is a non-profit variant |

## Demographics — handle with care

`Race`, `Ethnicity`, `Gender`, `Veteran` — self-reported **and optional**. The overwhelmingly
most common value is **"Unanswered"**, which makes naive group-by comparisons misleading:
you're mostly comparing "answered" vs "didn't answer," not group vs group. If you use these
columns in a finding, say what fraction is Unanswered first.

## Lenders

| Column | What it is |
|---|---|
| `OriginatingLender` (+ `City`, `State`, `LocationID`) | The lender that made the loan |
| `ServicingLenderName` (+ address fields, `LocationID`) | The lender currently servicing it |

## How the money was used (`*_PROCEED` columns)

`UTILITIES_PROCEED`, `PAYROLL_PROCEED`, `MORTGAGE_INTEREST_PROCEED`, `RENT_PROCEED`,
`REFINANCE_EIDL_PROCEED`, `HEALTH_CARE_PROCEED`, `DEBT_INTEREST_PROCEED` — dollar amounts by
intended use, **lender-reported at origination**. Per the SBA: on the application these were
*checkboxes*, so the dollar splits are rough allocations, not audited spending. Mostly
`PAYROLL_PROCEED` (that was the point of the program); the rest are sparse.

---

*Everything here is public data released by the SBA under FOIA. Some businesses you'll recognize;
be a professional about it — analyze patterns, don't dunk on individual borrowers by name.*
