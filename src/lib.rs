use pyo3::prelude::*;

#[pymodule]
fn pludot(_m: &Bound<'_, PyModule>) -> PyResult<()> {
    Ok(())
}