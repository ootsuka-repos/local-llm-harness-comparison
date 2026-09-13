// The complete table and native popovers work without JavaScript.
// Position an opened cell's details beside its trigger, within the viewport.
const scroller = document.querySelector('.table-scroll');
const triggers = new Map(
  Array.from(document.querySelectorAll('table [popovertarget]'), button => [button.getAttribute('popovertarget'), button])
);
let activeDetail = null;

function positionDetail(detail, trigger) {
  const anchor = trigger.getBoundingClientRect();
  const gap = 8;
  const edge = 12;
  const width = Math.min(390, window.innerWidth - edge * 2);
  const height = Math.min(detail.scrollHeight + 2, window.innerHeight - edge * 2);
  let left = anchor.left + anchor.width / 2 - width / 2;
  let top = anchor.bottom + gap;
  if (top + height > window.innerHeight - edge) top = anchor.top - gap - height;
  left = Math.max(edge, Math.min(left, window.innerWidth - width - edge));
  top = Math.max(edge, Math.min(top, window.innerHeight - height - edge));
  Object.assign(detail.style, { margin: '0', left: `${left}px`, top: `${top}px`, right: 'auto', bottom: 'auto' });
}

for (const detail of document.querySelectorAll('.cell-detail')) {
  const trigger = triggers.get(detail.id);
  if (!trigger) continue;
  trigger.setAttribute('aria-haspopup', 'dialog');
  trigger.setAttribute('aria-expanded', 'false');
  detail.addEventListener('beforetoggle', event => {
    if (event.newState === 'open') {
      // Reset stale coordinates after a resize before the popover is painted.
      Object.assign(detail.style, { visibility: 'hidden', margin: '0', left: '12px', top: '12px', right: 'auto', bottom: 'auto' });
    }
  });
  detail.addEventListener('toggle', event => {
    const open = event.newState === 'open';
    trigger.setAttribute('aria-expanded', String(open));
    if (open) {
      activeDetail = detail;
      positionDetail(detail, trigger);
      detail.style.visibility = 'visible';
    } else if (activeDetail === detail) {
      activeDetail = null;
    }
  });
}

function closeDetail() {
  if (activeDetail?.matches(':popover-open')) activeDetail.hidePopover();
}
scroller.addEventListener('scroll', closeDetail, { passive: true });
window.addEventListener('resize', closeDetail, { passive: true });
