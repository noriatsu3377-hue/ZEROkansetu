document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Configuration & Dynamic Content Injection
    const injectConfigData = () => {
        if (typeof CONFIG === 'undefined') return;

        // Set URLs
        const setBtns = document.querySelectorAll('.dynamic-application-set');
        setBtns.forEach(btn => {
            if (CONFIG.APPLICATION_URL) btn.href = CONFIG.APPLICATION_URL;
        });

        // Basic URLs
        const basicBtns = document.querySelectorAll('.dynamic-application-basic');
        basicBtns.forEach(btn => {
            if (CONFIG.APPLICATION_URL_BASIC) btn.href = CONFIG.APPLICATION_URL_BASIC;
        });

        // Advance URLs
        const advanceBtns = document.querySelectorAll('.dynamic-application-advance');
        advanceBtns.forEach(btn => {
            if (CONFIG.APPLICATION_URL_ADVANCE) btn.href = CONFIG.APPLICATION_URL_ADVANCE;
        });

        // Basic Dates
        const basicDateEls = document.querySelectorAll('.dynamic-basic-dates');
        basicDateEls.forEach(el => {
            el.textContent = CONFIG.BASIC_DATES;
        });

        // Advance Dates
        const advanceDateEls = document.querySelectorAll('.dynamic-advance-dates');
        advanceDateEls.forEach(el => {
            el.textContent = CONFIG.ADVANCE_DATES;
        });

        // Venue
        const venueEls = document.querySelectorAll('.dynamic-venue');
        venueEls.forEach(el => {
            el.textContent = CONFIG.VENUE;
        });

        // Capacity
        const capacityEls = document.querySelectorAll('.dynamic-capacity');
        capacityEls.forEach(el => {
            el.textContent = CONFIG.CAPACITY;
        });
    };

    injectConfigData();

    // 2. Opening Animation Control
    const handleOpeningAnimation = () => {
        const hasSeenIntro = sessionStorage.getItem('zero_lp_intro_seen');
        
        if (hasSeenIntro) {
            // Skip animation if already seen in this session
            document.body.classList.add('is-loaded');
        } else {
            // Run animation and mark as seen
            setTimeout(() => {
                document.body.classList.add('is-loaded');
                sessionStorage.setItem('zero_lp_intro_seen', 'true');
            }, 3000); // Overlay disappears after 3 seconds
        }
    };

    handleOpeningAnimation();

    // 3. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal, .mask-reveal, .fade-up-text');
    
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    };

    const revealOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    
    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // 4. FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const isOpen = question.classList.contains('is-open');
            
            // Close all other accordions (Optional, un-comment if single-open is desired)
            /*
            faqQuestions.forEach(q => {
                q.classList.remove('is-open');
                q.nextElementSibling.style.maxHeight = null;
            });
            */

            if (isOpen) {
                question.classList.remove('is-open');
                answer.style.maxHeight = null;
            } else {
                question.classList.add('is-open');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });

    // 5. Fixed CTA Footer Visibility (Mobile)
    const fixedCta = document.querySelector('.fixed-cta-footer');
    const heroSection = document.querySelector('.hero-section');
    
    if (fixedCta && heroSection) {
        const ctaObserverCallback = (entries) => {
            entries.forEach(entry => {
                // Show fixed CTA only after scrolling past the hero section
                if (!entry.isIntersecting && entry.boundingClientRect.top < 0) {
                    fixedCta.classList.add('is-visible');
                } else {
                    fixedCta.classList.remove('is-visible');
                }
            });
        };

        const ctaObserver = new IntersectionObserver(ctaObserverCallback, {
            threshold: 0
        });

        ctaObserver.observe(heroSection);
    }
});
