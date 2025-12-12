"""
更新競品比較表格的CSS樣式以適應多欄位
"""

css_styles = '''

/* ===== 更新版競品比較表格樣式 (多欄位) ===== */
.comparison-table {
    min-width: 900px; /* 增加最小寬度以容納更多欄位 */
}

/* 調整欄位寬度 */
.feature-col {
    width: 15% !important;
}

.competitor-col {
    width: 13% !important;
    font-size: 0.95rem;
}

.our-product-col {
    width: 20% !important;
}

/* 調整表頭文字 */
.comparison-table th {
    font-size: 1rem;
    padding: 15px 10px;
}

.comparison-table td {
    padding: 15px 10px;
    font-size: 0.95rem;
}

/* 針對小螢幕優化 */
@media (max-width: 992px) {
    .comparison-table-wrapper {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }
    
    .comparison-table {
        min-width: 800px;
    }
}

/* 確保最佳選擇標籤不跑版 */
.best-choice-badge {
    width: max-content;
    white-space: nowrap;
}
'''

# 添加樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS updated: Multi-column comparison table styles")
