// Single source of truth for every figure on the page. Owner-supplied.
(function (root) {
  var D = {
    main2025: 9060764.00,
    main2026ytd: 7616437.00, // Jan 1 to Oct 20, 2026
    branches: 9,
    perBranchMonthly: 100000,
    feeRate: 0.05,
    fee2025: 540000.00,
    fee2026ytd: 433479.45 // Jan 1 to Oct 20, 2026
  };
  var c = function (n) { return Math.round(n * 100) / 100; };
  D.mainTotal = c(D.main2025 + D.main2026ytd);
  D.combinedMonthly = D.branches * D.perBranchMonthly;
  D.feeMonthly = c(D.combinedMonthly * D.feeRate);
  D.feeAnnual = c(D.feeMonthly * 12);
  D.feeTotal = c(D.fee2025 + D.fee2026ytd);
  D.grandTotal = c(D.mainTotal + D.feeTotal);
  D.peso = function (n, dec) {
    dec = dec === undefined ? 2 : dec;
    return "\u20B1" + n.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec });
  };
  if (typeof module !== "undefined") module.exports = D; else root.TA_DATA = D;
})(this);
