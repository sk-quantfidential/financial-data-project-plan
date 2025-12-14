# PR: Epic GWC-0003 - Candle Processing Shared Library

**Branch:** `feature/epic-GWC-0003-candle-processing`
**Target:** `main`
**Epic:** GWC-0003
**Components:** client-gw-core-py, coinbase-client-gw-py, okx-client-gw-py, project-plan

## Summary

Centralizes candle gap detection and interpolation logic in client-gw-core-py as a
shared library with Protocol-based interface. Exchange-specific implementations
(Coinbase, OKX) now conform to `CandleProtocol` and use factory pattern for
creating interpolated candles.

## What Changed

### client-gw-core-py

**New Files:**

| File | Purpose |
|------|---------|
| `src/client_gw_core/ports/candle.py` | CandleProtocol and CandleFactory protocols |
| `src/client_gw_core/services/candles_processing.py` | Gap detection, interpolation, and streaming |
| `tests/unit/test_candles_processing.py` | 20 comprehensive unit tests |

**CandleProtocol Definition:**

```python
@runtime_checkable
class CandleProtocol(Protocol):
    @property
    def timestamp(self) -> datetime: ...
    @property
    def time_delta(self) -> timedelta: ...
    @property
    def open(self) -> Numeric: ...  # float | Decimal
    @property
    def high(self) -> Numeric: ...
    @property
    def low(self) -> Numeric: ...
    @property
    def close(self) -> Numeric: ...
    @property
    def volume(self) -> Numeric: ...
```

**Processing Functions:**

| Function | Description |
|----------|-------------|
| `detect_gaps()` | Find gaps in candle sequences |
| `interpolate_candles[T]()` | Linear interpolation with factory pattern |
| `fill_missing_candles[T]()` | Batch gap filling |
| `stream_filled_candles[T]()` | Async generator for streaming with inline gap filling |

### coinbase-client-gw-py

**Modified Files:**

| File | Change |
|------|--------|
| `src/coinbase_client_gw/models/product.py` | Added `timestamp` property (alias for `time`) |
| `src/coinbase_client_gw/adapters/__init__.py` | Export CoinbaseCandleFactory |
| `src/coinbase_client_gw/apps/dump_candles_data.py` | Use shared library functions |

**New Files:**

| File | Purpose |
|------|---------|
| `src/coinbase_client_gw/adapters/candle_factory.py` | CoinbaseCandleFactory implementation |

### okx-client-gw-py

**Modified Files:**

| File | Change |
|------|--------|
| `src/okx_client_gw/domain/models/candle.py` | Added `time_delta` field, float accessor properties |
| `src/okx_client_gw/adapters/__init__.py` | Export OkxCandleFactory |

**New Files:**

| File | Purpose |
|------|---------|
| `src/okx_client_gw/adapters/candle_factory.py` | OkxCandleFactory implementation (float to Decimal) |

### project-plan

**Modified Files:**

| File | Change |
|------|--------|
| `TODO-MASTER.md` | Added Epic GWC-0003 tracking section |

## Design Decisions

**Canonical Time Field: `timestamp`**
- OKX already uses `timestamp`
- Coinbase adds property alias for `time` field
- Consistent interface across exchanges

**Granularity Field: `time_delta`**
- Required in protocol for gap detection
- Represents candle duration (e.g., `timedelta(hours=1)`)

**Factory Pattern:**
- `CandleFactory[T]` protocol for creating exchange-specific instances
- Interpolation returns same type as input candles
- OKX factory converts float to Decimal

**Numeric Type:**
- `Numeric = float | Decimal` union type
- Supports both Coinbase (float) and OKX (Decimal)

## Commits

### client-gw-core-py

| Commit | Type | Description |
|--------|------|-------------|
| `178a105` | feat(ports) | Add CandleProtocol and candle processing utilities |

### coinbase-client-gw-py

| Commit | Type | Description |
|--------|------|-------------|
| `c4d23c3` | feat(adapters) | Add CandleFactory and update CLI to use shared processing |

### okx-client-gw-py

| Commit | Type | Description |
|--------|------|-------------|
| `b2684e2` | feat(domain) | Add time_delta to Candle model and OkxCandleFactory |

### project-plan

| Commit | Type | Description |
|--------|------|-------------|
| `eda60a0` | docs(epics) | Add Epic GWC-0003 candle processing tracking |

## Testing

- [x] 20 new unit tests for candle processing (client-gw-core-py)
- [x] All 287 tests pass in client-gw-core-py
- [x] Ruff check passes on all modified files
- [x] CandleProtocol compliance verified for both exchanges

### Test Coverage

| Test Class | Tests | Coverage |
|------------|-------|----------|
| TestGapInfo | 1 | Frozen dataclass |
| TestDetectGaps | 5 | Empty, single, consecutive, gaps |
| TestInterpolateCandles | 5 | Zero/negative count, single/multiple, time_delta |
| TestFillMissingCandles | 5 | Empty, single, no gaps, single/multiple gaps |
| TestStreamFilledCandles | 4 | Empty, single, consecutive, gap filling |

## Breaking Changes

None - all changes are additive.

## Migration Guide

### For Coinbase Users

No changes required. The `timestamp` property is an alias - existing code using
`candle.time` continues to work.

### For OKX Users

Update candle creation to include `time_delta`:

```python
# Before
candle = Candle.from_okx_array(data)

# After
candle = Candle.from_okx_array(data, time_delta=timedelta(hours=1))
```

### Using Shared Processing

```python
from client_gw_core import detect_gaps, fill_missing_candles
from coinbase_client_gw.adapters import CoinbaseCandleFactory

# Detect gaps
gaps = detect_gaps(candles)

# Fill gaps with interpolation
factory = CoinbaseCandleFactory()
filled, count = fill_missing_candles(candles, factory)
```

## Related Issues

- Epic GWC-0003: Candle Processing Shared Library
- Epic GWC-0002: Generic Async HTTP/WebSocket Client Core (prerequisite)
