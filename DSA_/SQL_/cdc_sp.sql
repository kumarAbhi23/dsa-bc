--- incremrtal_load sp--

CREATE procedure sp_incremtal_laod 
(
    @table_name VARCHAR(50),
    @watermark DATETIME
   

)
AS 
BEGAIN

DECLARE @sql NVARCHAR(MAX)
SET @sql='SELECT * FROM '+@table_name +'
          WHERE 