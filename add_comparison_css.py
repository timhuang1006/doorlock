"""
添加競品比較表格的CSS樣式
"""

css_styles = '''

/* ===== 競品比較表格樣式 ===== */
.comparison-section {
    padding: 80px 0;
    background: #0a0a0a;
}

.comparison-table-wrapper {
    margin-top: 50px;
    overflow-x: auto;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    background: #1a1a1a;
    min-width: 600px;
}

.comparison-table th,
.comparison-table td {
    padding: 20px 25px;
    text-align: center;
    border-bottom: 1px solid #333;
}

/* 表頭樣式 */
.comparison-table th {
    font-size: 1.1rem;
    font-weight: 600;
    color: #fff;
    background: #222;
    position: relative;
}

.feature-col {
    text-align: left !important;
    width: 30%;
    color: #aaa !important;
}

.competitor-col {
    width: 35%;
    color: #ccc !important;
}

.our-product-col {
    width: 35%;
    color: #FFD700 !important;
    background: rgba(255, 215, 0, 0.1) !important;
    border-top: 3px solid #FFD700;
}

/* 最佳選擇標籤 */
.best-choice-badge {
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    background: #FFD700;
    color: #000;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 700;
    box-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
}

/* 內容樣式 */
.feature-name {
    text-align: left !important;
    color: #ddd;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 10px;
}

.feature-name i {
    color: #FFD700;
    width: 20px;
    text-align: center;
}

.competitor-val {
    color: #888;
}

.our-product-val {
    color: #fff;
    font-weight: 500;
    background: rgba(255, 215, 0, 0.03);
}

.highlight-text {
    color: #FFD700;
    font-weight: 700;
}

.text-muted {
    color: #555;
    font-size: 0.9rem;
}

/* 響應式調整 */
@media (max-width: 768px) {
    .comparison-table th,
    .comparison-table td {
        padding: 15px 10px;
        font-size: 0.9rem;
    }
    
    .feature-name i {
        display: none;
    }
    
    .best-choice-badge {
        font-size: 0.7rem;
        padding: 2px 8px;
    }
}
'''

# 添加樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS added: Comparison table styles")
