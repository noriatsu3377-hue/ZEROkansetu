with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Differentiation Section */
.differentiation-section {
    background-color: var(--c-black-2);
    color: var(--c-white-1);
    padding: 8rem 0;
}

.diff-intro-title {
    font-size: 1.8rem;
    font-family: var(--font-serif);
    line-height: 1.5;
    margin-bottom: 3rem;
    color: var(--c-accent);
}

.diff-intro-text p {
    font-size: 1.05rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.diff-sub-title {
    font-size: 1.4rem;
    margin-bottom: 1.5rem;
    border-left: 3px solid var(--c-accent);
    padding-left: 1rem;
    color: var(--c-white-1);
}

.diff-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    padding: 2.5rem;
}

.highlight-card {
    background: rgba(142,23,27,0.05);
    border: 1px solid rgba(142,23,27,0.2);
}

.diff-list {
    list-style: none;
    padding: 0;
}

.diff-list li {
    font-size: 1rem;
    margin-bottom: 0.8rem;
    padding-left: 1.5rem;
    position: relative;
    color: var(--c-gray-1);
}

.diff-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.7em;
    width: 6px;
    height: 1px;
    background-color: var(--c-accent);
}

.diff-lead {
    font-size: 1.2rem;
    line-height: 1.6;
    color: var(--c-white-1);
}

.diff-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    list-style: none;
    padding: 0;
}

.diff-tags li {
    background: rgba(255,255,255,0.05);
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
    border-radius: 20px;
    color: var(--c-gray-1);
}

.diff-bold-text {
    font-size: 1.1rem;
    line-height: 1.7;
    color: var(--c-white-1);
}

/* Responsive Table / Cards for mobile */
.diff-table th, .diff-table td {
    padding: 1.2rem;
}

.diff-table .zero-col {
    background: rgba(142,23,27,0.05);
    font-weight: 600;
}

.diff-table .table-label-col {
    width: 15%;
    font-weight: bold;
    color: var(--c-accent);
}

@media (max-width: 768px) {
    .diff-table thead {
        display: none;
    }
    .diff-table tr {
        display: flex;
        flex-direction: column;
        margin-bottom: 2rem;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.05);
    }
    .diff-table td {
        display: block;
        width: 100%;
        border: none;
        padding: 1rem 1.5rem;
    }
    .diff-table td::before {
        content: attr(data-label);
        display: block;
        font-size: 0.8rem;
        color: var(--c-gray-2);
        margin-bottom: 0.3rem;
    }
    .diff-table .table-label-col {
        background: rgba(255,255,255,0.05);
        color: var(--c-white-1);
        text-align: center;
        font-size: 1.1rem;
    }
    .diff-table .table-label-col::before {
        display: none;
    }
}

.diff-outro-text {
    font-size: 1.1rem;
    line-height: 2;
    color: var(--c-white-1);
}

/* Animations */
.mask-reveal {
    overflow: hidden;
}
.mask-reveal span {
    display: inline-block;
    transform: translateY(100%);
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.mask-reveal.is-visible span {
    transform: translateY(0);
}

.fade-up-text {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.8s ease, transform 0.8s ease;
}
.fade-up-text.is-visible {
    opacity: 1;
    transform: translateY(0);
}
""")
