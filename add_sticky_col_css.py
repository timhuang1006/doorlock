"""
添加釘選欄位 (Sticky Column) 的 CSS 樣式
"""

css_styles = '''

/* ===== 釘選欄位樣式 ===== */
.sticky-col {
    position: sticky;
    left: 0;
    z-index: 10;
    box-shadow: 4px 0 10px rgba(0, 0, 0, 0.5); /* 添加陰影區隔 */
}

/* 確保表頭的釘選層級最高 */
th.sticky-col {
    z-index: 11;
}

/* 針對手機版的優化 */
@media (max-width: 992px) {
    .comparison-table-wrapper {
        padding-left: 0; /* 移除左側內距以確保貼齊 */
    }
    
    /* 確保釘選欄位背景不透明，避免文字重疊 */
    .our-product-col, 
    .our-product-val {
        background-color: #1a1a1a !important; /* 與表格背景一致 */
    }
    
    /* 恢復高亮背景色，但使用偽元素或漸層來模擬，或者直接使用較深的背景 */
    .our-product-col {
        background-color: #222 !important;
        border-right: 1px solid #333;
    }
    
    .our-product-val {
        background-color: #1e1e1e !important;
        border-right: 1px solid #333;
    }
}
'''

# 添加樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS added: Sticky column styles")
