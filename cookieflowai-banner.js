/**
 * CookieFlowAI Consent Banner
 * Site key: site_ce0bf460b3ec3264df2116afef5759d54c28
 * Installed on: clickflowgrow.com
 */
(function () {
  'use strict';

  var SITE_KEY = 'site_ce0bf460b3ec3264df2116afef5759d54c28';
  var BANNER_REGION = 'gdpr_uk';
  var CONSENT_KEY = 'cfai_consent';
  var VISITOR_KEY = 'cfai_visitor_id';
  var CONSENT_API = 'https://cookieflowai.com/api/public/consent';
  var PRIVACY_URL = 'https://clickflowgrow.com/privacy-policy.html';
  var COOKIE_URL = 'https://clickflowgrow.com/cookie-policy.html';

  function generateId() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0;
      return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
  }

  function getVisitorId() {
    var id = localStorage.getItem(VISITOR_KEY);
    if (!id) { id = generateId(); localStorage.setItem(VISITOR_KEY, id); }
    return id;
  }

  function hasConsented() {
    return !!localStorage.getItem(CONSENT_KEY);
  }

  function saveConsent(choices) {
    localStorage.setItem(CONSENT_KEY, JSON.stringify({ ts: Date.now(), choices: choices }));
  }

  function postConsent(choices, mode) {
    var payload = {
      publicSiteKey: SITE_KEY,
      visitorId: getVisitorId(),
      bannerRegion: BANNER_REGION,
      consentMode: mode || 'opt_in',
      choices: choices
    };
    fetch(CONSENT_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }).catch(function () {});
    document.dispatchEvent(new CustomEvent('cookieflowai:consent-updated', { detail: choices }));
  }

  function removeBanner() {
    var el = document.getElementById('cfai-banner');
    if (el) el.remove();
    var overlay = document.getElementById('cfai-overlay');
    if (overlay) overlay.remove();
  }

  function acceptAll() {
    var choices = { necessary: true, performance: true, functional: true, marketing: true };
    saveConsent(choices);
    postConsent(choices, 'opt_in');
    removeBanner();
  }

  function rejectAll() {
    var choices = { necessary: true, performance: false, functional: false, marketing: false };
    saveConsent(choices);
    postConsent(choices, 'opt_out');
    removeBanner();
  }

  function showPreferences() {
    var overlay = document.getElementById('cfai-overlay');
    if (overlay) overlay.style.display = 'flex';
  }

  function savePreferences() {
    var perf = document.getElementById('cfai-pref-performance');
    var func = document.getElementById('cfai-pref-functional');
    var mkt = document.getElementById('cfai-pref-marketing');
    var choices = {
      necessary: true,
      performance: perf ? perf.checked : false,
      functional: func ? func.checked : false,
      marketing: mkt ? mkt.checked : false
    };
    var allOn = choices.performance && choices.functional && choices.marketing;
    saveConsent(choices);
    postConsent(choices, allOn ? 'opt_in' : 'opt_out');
    removeBanner();
  }

  function renderBanner() {
    var style = document.createElement('style');
    style.textContent = [
      '#cfai-banner{position:fixed;bottom:0;left:0;right:0;z-index:99999;background:#0A0745;color:#EAE6DC;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:14px;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;box-shadow:0 -2px 16px rgba(0,0,0,.35);}',
      '#cfai-banner p{margin:0;flex:1 1 300px;line-height:1.5;}',
      '#cfai-banner a{color:#00AD9C;text-decoration:underline;}',
      '#cfai-banner-btns{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}',
      '.cfai-btn{border:none;border-radius:6px;padding:9px 18px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;}',
      '.cfai-btn-accept{background:#00AD9C;color:#fff;}',
      '.cfai-btn-reject{background:transparent;color:#EAE6DC;border:1px solid rgba(234,230,220,.4);}',
      '.cfai-btn-prefs{background:transparent;color:#EAE6DC;border:1px solid rgba(234,230,220,.4);}',
      '#cfai-overlay{display:none;position:fixed;inset:0;z-index:100000;background:rgba(0,0,0,.6);align-items:center;justify-content:center;}',
      '#cfai-modal{background:#fff;color:#0A0745;border-radius:12px;padding:28px 32px;max-width:480px;width:90%;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}',
      '#cfai-modal h3{margin:0 0 16px;font-size:18px;color:#0A0745;}',
      '.cfai-pref-row{display:flex;align-items:flex-start;justify-content:space-between;padding:10px 0;border-bottom:1px solid #eee;gap:12px;}',
      '.cfai-pref-row:last-of-type{border-bottom:none;}',
      '.cfai-pref-label{font-weight:600;font-size:14px;margin-bottom:2px;}',
      '.cfai-pref-desc{font-size:12px;color:#666;margin:0;}',
      '.cfai-toggle{position:relative;width:40px;height:22px;flex-shrink:0;}',
      '.cfai-toggle input{opacity:0;width:0;height:0;}',
      '.cfai-slider{position:absolute;inset:0;background:#ccc;border-radius:22px;cursor:pointer;transition:.3s;}',
      '.cfai-slider:before{content:"";position:absolute;height:16px;width:16px;left:3px;bottom:3px;background:#fff;border-radius:50%;transition:.3s;}',
      '.cfai-toggle input:checked+.cfai-slider{background:#00AD9C;}',
      '.cfai-toggle input:checked+.cfai-slider:before{transform:translateX(18px);}',
      '.cfai-toggle input:disabled+.cfai-slider{opacity:.6;cursor:not-allowed;}',
      '#cfai-modal-btns{display:flex;gap:8px;justify-content:flex-end;margin-top:20px;}',
      '.cfai-btn-save{background:#0A0745;color:#fff;}'
    ].join('');
    document.head.appendChild(style);

    var banner = document.createElement('div');
    banner.id = 'cfai-banner';
    banner.innerHTML = '<p>We use cookies to improve your experience. See our <a href="' + COOKIE_URL + '">Cookie Policy</a> and <a href="' + PRIVACY_URL + '">Privacy Policy</a>.</p>' +
      '<div id="cfai-banner-btns">' +
      '<button class="cfai-btn cfai-btn-prefs" onclick="window.__cfaiPrefs()">Manage Preferences</button>' +
      '<button class="cfai-btn cfai-btn-reject" onclick="window.__cfaiReject()">Reject All</button>' +
      '<button class="cfai-btn cfai-btn-accept" onclick="window.__cfaiAccept()">Accept All</button>' +
      '</div>';
    document.body.appendChild(banner);

    var overlay = document.createElement('div');
    overlay.id = 'cfai-overlay';
    overlay.innerHTML = '<div id="cfai-modal">' +
      '<h3>Cookie Preferences</h3>' +
      '<div class="cfai-pref-row"><div><p class="cfai-pref-label">Necessary</p><p class="cfai-pref-desc">Required for the site to function. Cannot be disabled.</p></div><label class="cfai-toggle"><input type="checkbox" id="cfai-pref-necessary" checked disabled><span class="cfai-slider"></span></label></div>' +
      '<div class="cfai-pref-row"><div><p class="cfai-pref-label">Performance</p><p class="cfai-pref-desc">Help us understand how visitors use the site.</p></div><label class="cfai-toggle"><input type="checkbox" id="cfai-pref-performance" checked><span class="cfai-slider"></span></label></div>' +
      '<div class="cfai-pref-row"><div><p class="cfai-pref-label">Functional</p><p class="cfai-pref-desc">Enable enhanced functionality and personalisation.</p></div><label class="cfai-toggle"><input type="checkbox" id="cfai-pref-functional" checked><span class="cfai-slider"></span></label></div>' +
      '<div class="cfai-pref-row"><div><p class="cfai-pref-label">Marketing</p><p class="cfai-pref-desc">Used to deliver relevant ads and track campaigns.</p></div><label class="cfai-toggle"><input type="checkbox" id="cfai-pref-marketing"><span class="cfai-slider"></span></label></div>' +
      '<div id="cfai-modal-btns"><button class="cfai-btn cfai-btn-reject" onclick="document.getElementById(\'cfai-overlay\').style.display=\'none\'">Cancel</button><button class="cfai-btn cfai-btn-save" onclick="window.__cfaiSave()">Save Preferences</button></div>' +
      '</div>';
    document.body.appendChild(overlay);
  }

  window.__cfaiAccept = acceptAll;
  window.__cfaiReject = rejectAll;
  window.__cfaiPrefs = showPreferences;
  window.__cfaiSave = savePreferences;

  if (hasConsented()) return;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderBanner);
  } else {
    renderBanner();
  }
})();
