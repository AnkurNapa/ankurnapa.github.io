---
layout: post
title: "Responsible Recommenders: Harm Caps, Consent-Aware Features and Why the Heaviest Drinkers Should Not Get the Best Offers"
image: /assets/og/responsible-recommenders-harm-caps-consent.png
description: "Part 3 of Responsible AI for Beer, Whisky and Wine. A recommender tuned for clicks and volume quietly over-serves the top decile of drinkers. How to fix it with harm-aware re-ranking, frequency caps, low and no-alcohol swaps, age gating, a consent-filtered feature view with purpose tags, and an offline eval that measures who the model is really talking to. With India's DPDP Act and Rules and GDPR in view."
date: 2026-09-26 09:00:00 -0700
updated: 2026-09-26
tags: [sales-intelligence, rai-beverage, recommender-systems, data-privacy, consent]
faq:
  - q: "Why is a normal recommender risky for an alcohol business?"
    a: "Because it learns from engagement and purchase volume, and in alcohol a small share of customers buys a large share of the volume. A model that optimises clicks or basket value will learn to aim its best offers, bigger packs and stronger products at the heaviest buyers. Nobody designed that. It falls out of the objective."
  - q: "What is harm-aware re-ranking?"
    a: "It is a rule layer after the model. The model scores products as usual, then the re-ranker applies policy: no stronger or bigger-pack upsells to high-frequency buyers, a cap on how often anyone sees alcohol promotions, a low or no-alcohol option in every slate, and no recommendations at all for anyone not age-verified. The rules are plain code, reviewed like any other policy."
  - q: "How do India's DPDP Act and Rules affect drinks recommenders?"
    a: "The DPDP Act 2023 requires consent for a specified purpose, and the DPDP Rules notified on 14 November 2025 phase in over time: the Data Protection Board first, consent manager registration from 14 November 2026, and the remaining substantive obligations from 14 May 2027. In practice that means tagging every feature with the purpose it was collected for and building the recommender only from features whose purpose covers personalisation."
---

**Short answer: a recommender trained to maximise clicks or basket value will, left alone, point its best offers at the people who already drink the most. In alcohol, a small slice of customers buys a large share of the volume, so the objective function finds them fast. The fix is not a better model. It is a policy layer after the model: no stronger or bigger-pack upsells to high-frequency buyers, frequency caps on alcohol promotions, a low or no-alcohol option in every slate, and no recommendations for anyone who has not passed an age gate. Under that sits a feature store where every column carries the purpose it was consented for, so the model can only learn from data the drinker agreed to share for personalisation. Then you measure it: what share of recommendations lands on the heaviest segment, before and after.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A recommender pipeline in four stages. Stage one is a consent-filtered feature view: raw loyalty, order and app data pass through a purpose filter so only features consented for personalisation reach the model. Stage two is the model, which scores products for each customer. Stage three is a harm-aware re-ranker with four rules: an age gate, no stronger or bigger-pack upsells for high-frequency buyers, a weekly frequency cap on alcohol promotions, and a low or no-alcohol option in every slate. Stage four is the slate the customer sees. Below, an offline eval compares the share of recommendations reaching the heaviest decile before and after the re-ranker, falling from 41 percent to 12 percent in the illustrative example.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE MODEL RANKS &#183; THE POLICY DECIDES WHO SEES WHAT</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="210" height="170" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="135" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">1. CONSENTED FEATURES</text>
<text x="48" y="110" font-size="10.5" fill="#4a6b64">loyalty &#183; orders &#183; app</text>
<text x="48" y="132" font-size="10.5" fill="#4a6b64">purpose tag per column</text>
<text x="48" y="154" font-size="10.5" fill="#4a6b64">filter: personalisation</text>
<text x="48" y="176" font-size="10.5" fill="#4a6b64">withdrawn consent drops</text>
<text x="48" y="198" font-size="10.5" fill="#4a6b64">the row, not just a flag</text>
<rect x="270" y="56" width="190" height="170" rx="9" fill="#06483f"/>
<text x="365" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">2. MODEL</text>
<text x="288" y="112" font-size="10.5" fill="#cfe6df">scores every product</text>
<text x="288" y="134" font-size="10.5" fill="#cfe6df">for every customer</text>
<text x="288" y="164" font-size="10.5" fill="#cfe6df">optimises what you</text>
<text x="288" y="186" font-size="10.5" fill="#cfe6df">told it to: clicks,</text>
<text x="288" y="208" font-size="10.5" fill="#cfe6df">basket value</text>
<rect x="490" y="56" width="280" height="170" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="630" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">3. HARM-AWARE RE-RANKER</text>
<text x="508" y="110" font-size="10.5" fill="#06483f">a. no age gate, no slate</text>
<text x="508" y="136" font-size="10.5" fill="#06483f">b. no stronger or bigger-pack</text>
<text x="524" y="152" font-size="10.5" fill="#06483f">upsell to high-frequency buyers</text>
<text x="508" y="178" font-size="10.5" fill="#06483f">c. weekly cap on alcohol promos</text>
<text x="508" y="204" font-size="10.5" fill="#06483f">d. one low or no-alc option always</text>
<rect x="800" y="56" width="170" height="170" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="885" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">4. THE SLATE</text>
<text x="818" y="112" font-size="10.5" fill="#4a6b64">what the drinker</text>
<text x="818" y="134" font-size="10.5" fill="#4a6b64">actually sees</text>
<text x="818" y="164" font-size="10.5" fill="#4a6b64">every rule that fired</text>
<text x="818" y="186" font-size="10.5" fill="#4a6b64">is logged with it</text>
<line x1="240" y1="141" x2="270" y2="141" stroke="#2e9e7c" stroke-width="2.5"/>
<line x1="460" y1="141" x2="490" y2="141" stroke="#2e9e7c" stroke-width="2.5"/>
<line x1="770" y1="141" x2="800" y2="141" stroke="#2e9e7c" stroke-width="2.5"/>
<rect x="30" y="252" width="940" height="74" rx="9" fill="#ffffff" stroke="#4db6a2" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="50" y="276" font-size="11" font-weight="700" fill="#00695c">OFFLINE EVAL &#183; share of promo impressions reaching the heaviest 10 percent of buyers</text>
<rect x="50" y="290" width="410" height="20" rx="4" fill="#ff4081"/>
<text x="470" y="305" font-size="10.5" fill="#06483f">model only: 41%</text>
<rect x="590" y="290" width="120" height="20" rx="4" fill="#2e9e7c"/>
<text x="720" y="305" font-size="10.5" fill="#06483f">with re-ranker: 12%</text>
<rect x="30" y="338" width="940" height="32" rx="10" fill="#06483f"/>
<text x="500" y="359" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">ILLUSTRATIVE NUMBERS &#183; MEASURE YOUR OWN BEFORE AND AFTER</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The model can stay as it is. The two layers around it, consented features in and policy out, are where responsibility lives.</figcaption>
</figure>

Picture a taproom loyalty app that sends its "you might also like" push to the same twelve regulars every Friday at five. Nobody set it up that way. The model simply learned that those twelve open the notification, and open it fast. Ask the bar staff about those twelve and, in most taprooms I know, they will name two or three they are already quietly worried about.

That is the problem with recommenders in drinks. The technique is ordinary. [Collaborative filtering, content features, a ranking model]({{ '/2021/beer-recommendation-engines/' | relative_url }}): the same stack that recommends shoes. The product is not ordinary. In most alcohol markets a small share of drinkers buys a large share of the volume, and any model rewarded for engagement or basket value will find that share and lean on it.

[Part 1]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}) put recommenders on the use-case register as a medium-risk system. [Part 2]({{ '/2026/genai-alcohol-marketing-guardrails-age-codes/' | relative_url }}) covered the words and images of alcohol marketing. This one covers the targeting: who the model decides to talk to, and what it offers them.

## How a well-meaning objective finds the heaviest drinkers

Take a whisky e-commerce site. The ranking model is trained on clicks and add-to-basket events and scored on revenue per session. Three things happen, none of them designed.

1. **Frequency wins.** The customer who buys every week generates ten times the training signal of the one who buys at Diwali and Christmas. The model gets very good at the frequent buyer.
2. **Upsell looks like success.** Offering the 1-litre bottle instead of the 70 cl, or the cask-strength release instead of the 40 percent one, lifts basket value. The model learns to do it most to the people most likely to say yes.
3. **Timing sharpens.** If the logs show a customer buys on Friday evenings, the model learns Friday evening. Push notifications land when resistance is lowest.

Each step is what a recommender is supposed to do. Put together, the heaviest decile gets the most offers, the strongest products and the best timing. A wine club's "reorder your favourites" email and a brewery app's "double your points on a 24-pack" do the same thing with different labels.

The model is not wrong. It is doing exactly what the objective asked. That is why the fix sits outside it.

## Layer 1: a feature view that only contains consented data

Before any ranking logic, decide what the model is allowed to learn from. A drinks business usually holds more than it should use: loyalty scans, app location pings, card-linked offers, taproom visit times, sometimes birthday and postcode. Not all of it was collected with personalisation in mind.

The lazy and correct pattern is a purpose tag on every column in the feature store and a view that joins only features whose purpose covers personalisation, for customers whose consent is current and age check has passed. Withdrawn consent removes the row. It does not set a flag the model can still see.

```sql
-- Feature catalogue: one row per feature, with the purpose it was collected for.
-- feature_catalogue(feature_name, source_table, purpose, sensitivity)
-- purpose in ('order_fulfilment','personalisation','analytics_aggregate','legal')

CREATE VIEW reco_features_v AS
SELECT
    c.customer_id,
    f.orders_90d,
    f.avg_basket_abv,
    f.preferred_styles,
    f.last_order_at
FROM customers c
JOIN consent_ledger k
  ON k.customer_id = c.customer_id
  AND k.purpose     = 'personalisation'
  AND k.status      = 'granted'
  AND k.withdrawn_at IS NULL
JOIN customer_features f
  ON f.customer_id = c.customer_id
WHERE c.age_verified = TRUE
  AND c.age_verified_at >= CURRENT_DATE - INTERVAL '365 days';

-- Guard test: fails the pipeline if the view uses a column not tagged for personalisation.
SELECT column_name
FROM information_schema.view_column_usage u
LEFT JOIN feature_catalogue fc
  ON fc.feature_name = u.column_name
 AND fc.purpose = 'personalisation'
WHERE u.view_name = 'reco_features_v'
  AND u.table_name = 'customer_features'
  AND fc.feature_name IS NULL;   -- any row returned = build fails
```

Notice what is missing. No precise location, no visit time of day, no inferred life events. They might lift click-through by a point. They are also the features that let a model learn "Friday at five, near the off-licence". Data minimisation is not only a legal duty here. It removes the sharpest tools for the wrong kind of targeting.

## The law this lines up with

In India, the Digital Personal Data Protection Act 2023 is built around consent for a specified purpose. The DPDP Rules were notified on 14 November 2025 and phase in over roughly eighteen months: the Data Protection Board of India from 14 November 2025, consent manager registration and related provisions from 14 November 2026, and the remaining substantive obligations from 14 May 2027. Consent managers, the intermediaries that let people give and withdraw consent across services, must be Indian companies. At the time of writing, September 2026, the practical message for a drinks business is simple: the purpose-tagged feature store you build now is the one the 2027 obligations will expect.

If you sell to drinkers in the EU or UK, GDPR already asks for the same shape: a lawful basis per purpose, data minimisation, and a right to object to direct marketing, including profiling for it. One design serves both.

This is not legal advice. It is the data model that makes legal advice cheap to follow.

## Layer 2: harm-aware re-ranking

The model scores products for a customer. The re-ranker takes that list and applies policy before anything is shown. It is plain code, reviewed by someone from compliance and someone from the trade, versioned like any other rule.

```python
from dataclasses import dataclass

HIGH_FREQ_ORDERS_90D = 12      # policy value, set by compliance, not by the model
WEEKLY_PROMO_CAP = 2

@dataclass(frozen=True)
class Item:
    sku: str
    abv: float
    pack_ml: int
    is_low_no: bool
    score: float

def rerank(items, customer, current_sku_abv, current_pack_ml, promos_this_week):
    """Return the slate to show, plus the list of rules that fired (for the log)."""
    fired = []
    if not customer["age_verified"]:
        return [], ["age_gate"]
    if promos_this_week >= WEEKLY_PROMO_CAP:
        return [], ["weekly_cap"]

    ranked = sorted(items, key=lambda i: i.score, reverse=True)
    if customer["orders_90d"] >= HIGH_FREQ_ORDERS_90D:
        kept = [i for i in ranked
                if i.abv <= current_sku_abv and i.pack_ml <= current_pack_ml]
        if len(kept) < len(ranked):
            fired.append("no_upsell_high_freq")
        ranked = kept

    slate = ranked[:4]
    if not any(i.is_low_no for i in slate):
        low_no = [i for i in items if i.is_low_no]
        if low_no:
            slate = slate[:3] + [max(low_no, key=lambda i: i.score)]
            fired.append("low_no_slot")
    return slate, fired

if __name__ == "__main__":
    items = [Item("ipa-440", 6.5, 440, False, 0.9), Item("dipa-440", 8.2, 440, False, 0.95),
             Item("lager-24pk", 4.8, 7920, False, 0.8), Item("na-pale", 0.5, 330, True, 0.3),
             Item("pils-330", 4.8, 330, False, 0.6)]
    heavy = {"age_verified": True, "orders_90d": 20}
    slate, fired = rerank(items, heavy, 6.5, 440, 0)
    assert all(i.abv <= 6.5 and i.pack_ml <= 440 for i in slate)
    assert any(i.is_low_no for i in slate) and "no_upsell_high_freq" in fired
    assert rerank(items, {"age_verified": False, "orders_90d": 0}, 6.5, 440, 0) == ([], ["age_gate"])
    print("ok")
```

Four rules, each one boring on purpose.

- **Age gate.** No verified age, no slate. Not a softer slate, none.
- **No upsell to high-frequency buyers.** For customers above the frequency line, nothing stronger and nothing bigger than what they usually buy. Sideways is fine: a different style at the same strength. Up is not.
- **Weekly cap.** A ceiling on alcohol promotions per person per week, whatever the model thinks of their open rate.
- **A low or no-alcohol slot.** Every slate carries one. The [no-alcohol category]({{ '/2026/non-alcoholic-beer-go-to-market/' | relative_url }}) is a real business, and a drinker who clicks it has told you something useful.

The threshold of twelve orders in ninety days is a placeholder. Set yours from your own distribution, write down who chose it and why, and put it in the [use-case register]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}) next to the model. A policy number with no owner drifts upward the first quarter sales are soft.

## Layer 3: measure who the model is talking to

Most recommender evals stop at click-through and revenue. Add one question: what share of promotional impressions reaches the heaviest-buying segment? Replay last quarter's traffic through the old ranking and the new one, and compare.

```sql
-- Offline eval: share of promo impressions landing on the top decile by 90-day volume.
WITH deciles AS (
    SELECT customer_id,
           NTILE(10) OVER (ORDER BY litres_90d DESC) AS volume_decile
    FROM customer_volume_90d
)
SELECT r.policy_version,
       ROUND(100.0 * SUM(CASE WHEN d.volume_decile = 1 THEN 1 ELSE 0 END)
             / COUNT(*), 1)                           AS pct_to_top_decile,
       ROUND(AVG(r.slot_abv), 2)                       AS avg_recommended_abv,
       ROUND(100.0 * AVG(CASE WHEN r.is_low_no THEN 1 ELSE 0 END), 1) AS pct_low_no
FROM replay_impressions r
JOIN deciles d USING (customer_id)
GROUP BY r.policy_version;
```

If the top decile is, say, 10 percent of customers and gets 41 percent of the promotions under the old ranking, that is the finding. After the re-ranker it should drift towards its population share. Track it monthly on the same dashboard as revenue per session, so nobody can quietly trade one for the other.

You will lose some revenue per session. Say so up front, with the number, before anyone discovers it in a quarterly review.

## Three places this shows up

**The taproom loyalty app.** Points for visits and pints. The re-ranker caps visit-streak pushes, never offers "double points on your third pint tonight", and gives the house alcohol-free beer a permanent slot. The streak feature stays; the evening-timed nudge goes.

**The wine club.** "Reorder your favourites" is fine. "You finished your case in nine days, here is a bigger one" is the upsell rule firing, and it should not. Offer the same case, or a mixed half-case with a lower-alcohol white.

**Whisky e-commerce.** Limited releases drive clicks from collectors, who are often not heavy drinkers at all. Keep collector signals (bottles held, auctions watched) separate from consumption signals, so a buyer of one expensive bottle a year is not scored like one who buys a litre a week.

## Where this breaks

**Frequency is a proxy, not a diagnosis.** A heavy buyer might be a pub landlord, a party planner or a household of six. The rule is blunt on purpose, and it will sometimes under-serve a good customer. Allow a trade account flag that moves them out of the consumer recommender entirely.

**Age verification is only as good as the check.** A checkbox is not a gate. Tie the flag to whatever verification your market requires at sale, and expire it.

**The re-ranker is policy, and policy gets lobbied.** Every rule costs revenue, so every rule will be questioned. Version the thresholds, log every change and who approved it, and review them on a fixed date, not when someone asks.

**Consent tags rot.** A new column gets added to the feature table by someone in a hurry, untagged. The guard query above catches it only if it runs in the build. Make it a failing test, not a report.

**Measuring harm is hard.** Share of impressions to the heaviest decile is a proxy for "are we pushing the people who least need pushing". It is not a health outcome. Treat it as a floor, not proof of good behaviour.

## The bottom line

A drinks recommender is ordinary machine learning pointed at an unusual product. Left to its objective, it will find the heaviest drinkers and serve them best. The responsible version keeps the model and wraps it: in front, a consent-filtered feature view where every column carries its purpose, which is also what India's DPDP regime and GDPR expect; behind, a short, boring set of rules that stops upsells to high-frequency buyers, caps promotions, always offers a low or no-alcohol choice and shows nothing to anyone unverified. Then one metric, who the promotions actually reach, sits on the same dashboard as revenue. The model sees clicks. The bar staff see the twelve people who get the Friday push. Build for what the bar staff see.

Next: [when the model touches food safety]({{ '/2026/ai-food-safety-human-release-model-cards/' | relative_url }}). The full list is on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**Why is a normal recommender risky for an alcohol business?**
Because it learns from engagement and purchase volume, and in alcohol a small share of customers buys a large share of the volume. A model that optimises clicks or basket value will learn to aim its best offers, bigger packs and stronger products at the heaviest buyers. Nobody designed that. It falls out of the objective.

**What is harm-aware re-ranking?**
It is a rule layer after the model. The model scores products as usual, then the re-ranker applies policy: no stronger or bigger-pack upsells to high-frequency buyers, a cap on how often anyone sees alcohol promotions, a low or no-alcohol option in every slate, and no recommendations at all for anyone not age-verified. The rules are plain code, reviewed like any other policy.

**How do India's DPDP Act and Rules affect drinks recommenders?**
The DPDP Act 2023 requires consent for a specified purpose, and the DPDP Rules notified on 14 November 2025 phase in over time: the Data Protection Board first, consent manager registration from 14 November 2026, and the remaining substantive obligations from 14 May 2027. In practice that means tagging every feature with the purpose it was collected for and building the recommender only from features whose purpose covers personalisation.
