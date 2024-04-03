import pyarrow as pa
import pyarrow.parquet as pq
import os
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    # Convert column names to lowercase
    data.columns = data.columns.str.lower()

    # Convert column names to snake case
    data.columns = data.columns.str.replace(' ', '_')

    # Delete unnecessary columns
    data = data.loc[:, ~data.columns.isin(['serial_number','location','opm_remarks', 'assessor_remarks', 'non_use_code'])]

    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
